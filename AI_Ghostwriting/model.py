import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Set path to your local Mistral 7B v0.3 model
MODEL_PATH = r"C:/mistral_models/7B-Instruct-v0.3"

def load_model():
    """Loads the Mistral 7B model and tokenizer from local storage."""
    print("Loading tokenizer from local directory...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)

    print("Loading model from local directory...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,  # Optimized for efficiency
        device_map="auto"  # Automatically assigns to CPU/GPU
    )
    return model, tokenizer

def generate_text(prompt, model, tokenizer):
    """Generates text using the local Mistral model."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_length=256,
            temperature=0.7,
            do_sample=True,
            top_k=50,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id
        )

    return tokenizer.decode(output[0], skip_special_tokens=True)
