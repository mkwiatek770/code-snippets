import os
import json
import sys
from tqdm import tqdm

dirs = ["biorxiv_medrxiv", "comm_use_subset", "noncomm_use_subset"]
articles = []

path = f"kaggle_data/{dirs[0]}/{dirs[0]}/pdf_json"
for file_ in tqdm(os.listdir(path)):
    with open(f"{path}/{file_}") as f:
        articles.append(json.load(f))


print(sys.getsizeof(articles))
print(articles[5])
print(len(articles))
