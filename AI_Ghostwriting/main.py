from model import load_model, generate_text
from auto_typing import auto_type

# Load model & tokenizer
model, tokenizer = load_model()

while True:
    user_input = input("\nEnter a prompt (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break

    generated_text = generate_text(user_input, model, tokenizer)
    print("\nGenerated Text:\n", generated_text)

    confirm = input("\nAuto-type this text? (y/n): ")
    if confirm.lower() == 'y':
        auto_type(generated_text)
