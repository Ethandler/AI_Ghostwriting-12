import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# We use a Mistral-7B model variant from HuggingFace.
# Note: The model identifier might change; for now, we use a common one.
model_name = "mistralai/Mistral-7B-Instruct-v0.1"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token="Your API Here")
print("Loading model... (this may take a while)")
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", use_auth_token="Your API here")

# Set the prompt for text generation.
prompt = "Write a short article about the importance of automation in modern business."
inputs = tokenizer(prompt, return_tensors="pt")

# If you have a GPU available, the model should auto-detect it.
if torch.cuda.is_available():
    inputs = inputs.to("cuda")

# Generate text with a maximum of 150 new tokens.
outputs = model.generate(**inputs, max_new_tokens=150)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("\n--- Generated Text ---\n")
print(generated_text)
print("\n----------------------\n")
