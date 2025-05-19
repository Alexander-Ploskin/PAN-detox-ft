import hydra
from omegaconf import OmegaConf
from loguru import logger
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import DataCollatorForSeq2Seq, Seq2SeqTrainer, Seq2SeqTrainingArguments
from datasets import load_dataset
from trl import SFTConfig, SFTTrainer
from utils.data import process_dataset
from utils.prompts import load_prompt
from utils.seeds import set_all_seeds
from peft import LoraConfig
import os 


@hydra.main(version_base=None, config_path="configs", config_name="main")
def train(cfg): 
    logger.info("Starting training with config:\n" + OmegaConf.to_yaml(cfg))
    os.environ["CUDA_VISIBLE_DEVICES"] = f'{cfg.device}'
    set_all_seeds(cfg.seed)
    
    model = hydra.utils.instantiate(cfg.model) 
    peft_config = hydra.utils.instantiate(cfg.peft) 
    tokenizer = hydra.utils.instantiate(cfg.tokenizer)
    training_args = hydra.utils.instantiate(cfg.training_args)
    
    ##### Refactor DS process code !!! #########
    dataset = load_dataset(cfg.dataset_path)['train']
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
            peft_config=peft_config if cfg.use_adapter else None
        )    
    else:
        raise NotImplementedError("Such trainer is not supported")
    
    logger.info(f"Running training")
    
    trainer.train()
    logger.info("Finished training")

if __name__ == "__main__": 
    train()