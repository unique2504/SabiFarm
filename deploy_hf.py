# deploy_hf.py
import os
from huggingface_hub import upload_folder

token = os.getenv("HF_TOKEN")
folders_to_upload = [
    'api', 'models', 'mobile', 'training',
    'requirements.txt', 'main.py', 'README.md'
]

for folder in folders_to_upload:
    upload_folder(
        folder_path=folder,
        path_in_repo=folder,
        repo_id='unique2504/farmsabi',
        token=token
    )
    print(f"Uploaded {folder} successfully!")

print("FarmSabi deployment completed successfully!")
