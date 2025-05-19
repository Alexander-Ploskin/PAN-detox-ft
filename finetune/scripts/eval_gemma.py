import torch
import pandas as pd
from tqdm import tqdm
import hydra
from transformers import Gemma3ForCausalLM, AutoTokenizer
from datasets import load_dataset
from collections import defaultdict
def submit(dataset, model, tokenizer, submit_file, max_length = 128):
    batches = []
    bs = 1
    for k, ds in dataset.items(): 
        curr = 0
        while curr < len(ds):
            messages = [ msg for msg  in ds[curr : min(curr + bs , len(ds)) ]['text'] ] 
            curr += bs 
            batches.append(messages)
    
    input_tensors = []
    input_tensors_len = []
    
    for batch in batches: 
        with torch.inference_mode():
            print(batch)
            inputs = tokenizer(batch, truncation = True, return_tensors = "pt", padding = True,  max_length = 128).to("cuda")
            input_tensors.append(inputs)
            input_tensors_len.append(inputs.input_ids.shape[-1])
    g_batches = defaultdict(list)
    g_ids = []
    for item in set(input_tensors_len):
    
        for id_, inp in enumerate(input_tensors): 
            if inp.input_ids.shape[-1] == item:
                g_batches[item].append(inp)
                g_ids.append(id_)
            
        input_ids = []
        attention_mask = []
    
        for elem in g_batches[item]:
            input_ids.append(elem['input_ids'])
            attention_mask.append(elem['attention_mask'])
        
        g_batches[item] = {
            'input_ids' : torch.concatenate(input_ids, 0), 
            'attention_mask' : torch.concatenate(attention_mask, 0)
        }

    detox = []
    for k, batch in tqdm( g_batches.items() ) : 
        with torch.inference_mode():
            #print(batch)
            generation = model.generate(**batch, max_new_tokens=128, do_sample=False)
            decoded = tokenizer.batch_decode(generation[..., k:], skip_special_tokens=True)
            detox.extend(decoded)
            #print(decoded)
    res = [0]*9000
    for i, item in enumerate( detox ) :
        res[g_ids[i]] = item
    
    submit = {
    
        'toxic_sentence' : [],
        'neutral_sentence' : [],
        'lang' : []
        
    }
    
    glob_cnt = 0 
    for lang, v in dataset.items(): 
        for item in tqdm(v): 
            submit['toxic_sentence'].append(item['text'])
            if res[glob_cnt] == '': 
                res[glob_cnt] = item['text']
            submit['neutral_sentence'].append(res[glob_cnt])
            submit['lang'].append(lang)
            glob_cnt += 1
            
    df = pd.DataFrame(submit)
    df.to_csv(submit_file, sep='\t', index=False)

@hydra.main(version_base=None, config_path="configs", config_name="eval_gemma")
def eval_model(cfg): 
    dataset = load_dataset(cfg.ds_path)
    model_id = cfg.model_ckpt
    
    model = Gemma3ForCausalLM.from_pretrained(
        model_id, device_map="auto", local_files_only = True
    ).eval()
    
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    submit(dataset, model, tokenizer, cfg.submit_file)

if __name__ == "__main__": 
    eval_model()





