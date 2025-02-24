from huggingface_hub import snapshot_download
from pathlib import Path

# Set the download directory to your D: drive
mistral_models_path = Path("D:/mistral_models/7B-Instruct-v0.3")
mistral_models_path.mkdir(parents=True, exist_ok=True)

# Replace with your actual token if needed
snapshot_download(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    local_dir=mistral_models_path,
    use_auth_token="API here"
)
