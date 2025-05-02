from transformers import AutoTokenizer, AutoModelForCausalLM

#download the model and tokenizer
model_name = "Qwen/Qwen2.5-0.5B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

#save model and tokenizer to disk
model_path ="./.cache/hf/Qwen/Qwen2.5-0.5B"
tokenizer.save_pretrained(model_path)
model.save_pretrained(model_path)
~                                