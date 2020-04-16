import os
import json
import sys

dirs = ["biorxiv_medrxiv", "comm_use_subset", "noncomm_use_subset"]
articles = []

path = f"kaggle_data/{dirs[0]}/{dirs[0]}/pdf_json"
for file_ in os.listdir(path):
    print(file_)
    with open(f"{path}/{file_}") as f:
        articles.append(json.load(f))


print(articles[5])
print(len(articles))
