python3 eval_gemma.py model_ckpt='gemma-lora-pt/checkpoint-500' submit_file="submits/lora_pt_500.tsv"
python3 eval_gemma.py model_ckpt='gemma-lora-pt/checkpoint-1000' submit_file="submits/lora_pt_1000.tsv"
python3 eval_gemma.py model_ckpt='gemma-lora-pt/checkpoint-1350' submit_file="submits/lora_pt_1350.tsv"

python3 eval_gemma.py model_ckpt='gemma-pt/checkpoint-500' submit_file="submits/pt_500.tsv"
python3 eval_gemma.py model_ckpt='gemma-pt/checkpoint-1000' submit_file="submits/pt_1000.tsv"
python3 eval_gemma.py model_ckpt='gemma-pt/checkpoint-1350' submit_file="submits/pt_1350.tsv"