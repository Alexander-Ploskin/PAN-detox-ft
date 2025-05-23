#python3 train.py device=0 model=gemma tokenizer=gemma trainer=sft training_args=sft training_args.output_dir='gemma-all-data'
#python3 train.py device=1 model=gemma tokenizer=gemma trainer=sft training_args=sft training_args.output_dir='gemma-all-data-lora' use_adapter=true
python3 train.py device=2 model=gemma tokenizer=gemma trainer=sft training_args=sft training_args.output_dir='gemma-filtered-final-paradetox' ds_list='final.csv'
#python3 train.py device=2 model=qwen tokenizer=qwen trainer=sft training_args=sft training_args/sft.output_dir='qwen-all-data'