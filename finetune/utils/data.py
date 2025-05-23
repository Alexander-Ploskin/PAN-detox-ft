from datasets import concatenate_datasets

def add_prompt_and_tokenize(examples, tokenizer, lang, lang_prompts, max_length = 128):
    toxic = [lang_prompts[lang] + tox for tox in examples['toxic_sentence']]

    inputs = tokenizer(toxic, truncation=True, padding = True, max_length=max_length)
    labels = tokenizer(examples['neutral_sentence'], truncation=True, padding = True, max_length=max_length)
    return {
        **inputs,
        'labels': labels.input_ids
    }

def process_dataset(tokenizer, dataset, lang_prompts): 
    for lang in dataset.keys():
        dataset[lang] = dataset[lang].map(lambda x : add_prompt_and_tokenize(x, tokenizer, lang, lang_prompts),  batched=True,)
        dataset[lang] =  dataset[lang].remove_columns(['toxic_sentence', 'neutral_sentence'])
    dataset = concatenate_datasets([item for (_, item) in dataset.items()]).shuffle()    
    return dataset

def preprocess_function(text, lang = None): 
    return {"prompt": text['toxic_comment'], "completion": text['neutral_comment']}

def process_dataset(dataset):
    dataset = dataset.map(lambda x : preprocess_function(x),  batched=False,)
    dataset = dataset.remove_columns(['toxic_comment', 'neutral_comment'])
    return dataset