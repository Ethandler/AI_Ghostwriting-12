import os
from huggingface_hub import snapshot_download
from pathlib import Path

# Retrieve your HF token from the environment
hf_token = os.getenv("HF_API_KEY", default=None)

# If you're sure they're not gated, you can comment this out:

# 2. whisper-large-v3
whisper_path = Path("D:/models/whisper-large-v3")
whisper_path.mkdir(parents=True, exist_ok=True)

# 3. fastchat-t5-3b-v1.0 (replaces TinyLlama)
fastchat_path = Path("D:/models/fastchat-t5-3b-v1.0")
fastchat_path.mkdir(parents=True, exist_ok=True)


# Download whisper-large-v3
snapshot_download(
    repo_id="openai/whisper-large-v3",
    local_dir=whisper_path,
    token=hf_token
)

# Download fastchat-t5-3b-v1.0
snapshot_download(
    repo_id="lmsys/fastchat-t5-3b-v1.0",
    local_dir=fastchat_path,
    token=hf_token
)

print("All downloads completed successfully!")
