from __future__ import absolute_import
import hydra
import os
from peft import LoraConfig
from omegaconf import OmegaConf
from loguru import logger
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import DataCollatorForSeq2Seq, Seq2SeqTrainer, Seq2SeqTrainingArguments
from datasets import load_dataset, concatenate_datasets
from trl import SFTConfig, SFTTrainer
from utils.data import process_dataset
from utils.prompts import load_prompt
from utils.seeds import set_all_seeds
import wandb

@hydra.main(version_base=None, config_path="configs", config_name="main")
def train(cfg): 
    logger.info("Starting training with config:\n" + OmegaConf.to_yaml(cfg))
    os.environ["CUDA_VISIBLE_DEVICES"] = f'{cfg.device}'
    set_all_seeds(cfg.seed)
    
    model = hydra.utils.instantiate(cfg.model) 
    peft_config = hydra.utils.instantiate(cfg.peft, _convert_="all") 
    print(peft_config)
    tokenizer = hydra.utils.instantiate(cfg.tokenizer)
    training_args = hydra.utils.instantiate(cfg.training_args)
    
    ##### Refactor DS process code !!! #########


    # https://huggingface.co/datasets/textdetox/multilingual_paradetox 
    # https://huggingface.co/datasets/s-nlp/paradetox 
    # https://huggingface.co/datasets/s-nlp/ru_paradetox 
    # https://huggingface.co/datasets/s-nlp/uk_paradetox
    # https://huggingface.co/datasets/s-nlp/es_paradetox
    # Assuming `cfg` is your Hydra DictConfig or ListConfig
    if not isinstance(cfg.ds_list, list):
        cfg.ds_list = [cfg.ds_list]
    datasets = []
    for item in cfg.ds_list: 
        if item == 'textdetox/multilingual_paradetox': 
            dataset = load_dataset(item)
            dataset = concatenate_datasets([item for (_, item) in dataset.items()]).shuffle()    
            dataset = dataset.rename_column("toxic_sentence", "toxic_comment")
            dataset = dataset.rename_column("neutral_sentence", "neutral_comment")
            print(f'[MULTILINGUAL PARADETOX] {dataset[0]}')
        elif item == 's-nlp/paradetox':
            dataset = load_dataset(item, split = 'train')
            dataset = dataset.rename_column("en_toxic_comment", "toxic_comment")
            dataset = dataset.rename_column("en_neutral_comment", "neutral_comment")
            print(f'[ENG PARADETOX] {dataset[0]}')
        elif item == 's-nlp/ru_paradetox':
            dataset = load_dataset(item, split = 'train')
            dataset = dataset.rename_column("ru_toxic_comment", "toxic_comment")
            dataset = dataset.rename_column("ru_neutral_comment", "neutral_comment")
            print(f'[RU PARADETOX] {dataset[0]}')
        elif item == 'textdetox/uk_paradetox':
            dataset = load_dataset(item, split = 'train')   
            dataset = dataset.rename_column("toxic_sentence", "toxic_comment")
            dataset = dataset.rename_column("neutral_sentence", "neutral_comment")
            print(f'[UK PARADETOX] {dataset[0]}')
        elif item == 'textdetox/es_paradetox':
            dataset = load_dataset(item, split = 'train')
            dataset = dataset.rename_column("toxic_sentence", "toxic_comment")
            dataset = dataset.rename_column("neutral_sentence", "neutral_comment")
            print(f'[ES PARADETOX] {dataset[0]}')
        elif item == 'data/mt0_detox_full_data':
            dataset = load_dataset('data', data_files='mt0_detox_full_data.csv', split = 'train')
            dataset = dataset.remove_columns(['split', 'lang'])
            print(f'[MT0 PARADETOX] {dataset[0]}')
        elif item == 'data/nikita_sushko':
            dataset = load_dataset('data', data_files='nikita-sushko-synth.csv', split = 'train')
            dataset = dataset.remove_columns(['Unnamed: 0', 'lang'])
            dataset = dataset.rename_column("toxic_sentence", "toxic_comment")
            dataset = dataset.rename_column("neutral_sentence", "neutral_comment")
            print(f'[NS PARADETOX] {dataset[0]}')
        else:
            dataset = load_dataset('cleaned', data_files=item, split = 'train')
            #dataset = dataset.remove_columns(['Unnamed: 0.1', 'Unnamed: 0', 'references', 'lang', 'J', 'STA', 'SIM', 'XCOMET'])
            #dataset = dataset.rename_column("neutral_sentence", "neutral_comment")
            #dataset = dataset.rename_column("toxic_sentence", "toxic_comment")
            print(f'[CUSTOM PARADETOX] {dataset[0]}')
        datasets.append(dataset)
    dataset = concatenate_datasets(datasets).shuffle()
    
    
    #dataset.push_to_hub("VladKozlovskiy/efficient-imagenet-tensorstorage")
    dataset = process_dataset(dataset)
    print(dataset[0])
    ##### Refactor DS process code !!! #########
    logger.info(f"Loaded dataset")
    


    ##### Due to https://github.com/omry/omegaconf/issues/144 #####
    if isinstance(training_args, Seq2SeqTrainingArguments):
        trainer = Seq2SeqTrainer(
            model=model,
            args=training_args,
            train_dataset=dataset 
        )
    elif isinstance(training_args, SFTConfig): 
        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=dataset, 
            peft_config= peft_config if cfg.use_adapter else None
        )    
    else:
        raise NotImplementedError("Such trainer is not supported")
    
    logger.info(f"Running training")
    
    trainer.train()
    logger.info("Finished training")

if __name__ == "__main__": 
    train()