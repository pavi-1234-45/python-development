from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda"

model_path = "ibm-granite/granite-4.0-h-350M-base"

tokenizer = AutoTokenizer.from_pretrained(model_path)
# drop device_map if running on CPU
model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device)
model.eval()
# change input text as desired
input_text = "The capital of France is"
# tokenize the text
input_tokens = tokenizer(input_text, return_tensors="pt").to(device)
# generate output tokens
output = model.generate(**input_tokens, max_length=10)
# decode output tokens into text
output = tokenizer.batch_decode(output)
# print output
print(output[0])
