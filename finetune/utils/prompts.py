import json 

def save_prompt(path, prompt): 
    with open(path, "w", encoding="utf-8") as f:
        json.dump(prompt, f, ensure_ascii=False, indent=2)

def load_prompt(path):  
    with open(path, "r", encoding="utf-8") as f:
        prompt = json.load(f)
    return prompt