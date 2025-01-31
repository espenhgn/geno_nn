#!/usr/bin/env python
# Downlowd weights and datasets from KaggleHub for offline use
import os
import keras
import kagglehub

# list of BERT models to download from KaggleHub
bert_model_path = ['keras/bert/keras/bert_tiny_en_uncased',
                   'keras/bert/keras/bert_small_en_uncased',
                   'keras/bert/keras/bert_medium_en_uncased',
                   'keras/bert/keras/bert_base_en_uncased',
                   'keras/bert/keras/bert_base_en',
                   ]

# Download selected version
for model in bert_model_path:
    path = kagglehub.model_download(model)
    print("Path to model files:", path)

    # move model files to parent directory
    destination_dir = os.path.join(os.getcwd(), path.split('.cache')[-1][1:])
    os.makedirs(destination_dir, exist_ok=True)
    os.system(f'cp -r {path}/* {destination_dir}/')
    print(f"Model {model} files copied to {destination_dir}/")

# load IMDB datasets (relative to ~/.keras/dataset)
_ = keras.datasets.imdb.load_data(path='imdb.npz')
_ = keras.datasets.imdb.get_word_index(path="imdb_word_index.json")

# move datasets to this directory
destination_dir = os.path.join(os.getcwd(), 'keras', 'datasets')
os.makedirs(destination_dir, exist_ok=True)
for imdb_file in ['imdb.npz', 'imdb_word_index.json']:
    os.system(f'cp ~/.keras/datasets/{imdb_file} {destination_dir}/')
    print(f"Dataset {imdb_file} copied to {destination_dir}/")
