#!/usr/env/bin python3

import os
import requests

def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

# define dictionary of model file names (GGUF files) and their corresponding download URLs
filenames_urls = {
    'Meta-Llama-3-8B-Instruct.Q4_0.gguf': 'https://huggingface.co/QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/resolve/main/Meta-Llama-3-8B-Instruct.Q4_0.gguf',
    'DeepSeek-R1-Distill-Llama-8B-Q8_0.gguf': 'https://huggingface.co/unsloth/DeepSeek-R1-Distill-Llama-8B-GGUF/resolve/main/DeepSeek-R1-Distill-Llama-8B-Q8_0.gguf'
}

model_path = os.path.join(os.getcwd(), 'weights')
os.makedirs(model_path, exist_ok=True)

for filename, url in filenames_urls.items():
    output_path = os.path.join(model_path, filename)
    if not os.path.exists(output_path):
        print(f"Downloading {filename} to {model_path}...")
        download_file(url, output_path)
        print(f"Downloaded {filename}")
    else:
        print(f"{output_path} already exists, skipping download")
