import os
import json
import sys
import pandas as pd
from tqdm import tqdm

dirs = ["biorxiv_medrxiv", "comm_use_subset", "noncomm_use_subset"]
articles = []

path = f"kaggle_data/{dirs[0]}/{dirs[0]}/pdf_json"
for file_ in tqdm(os.listdir(path)):
    with open(f"{path}/{file_}") as f:
        data = json.load(f)

        paper_id = data['paper_id']
        title = data['metadata']['title']

        full_abstract = ""
        for part in data['abstract']:
            full_abstract += part['text'] + "\n"

        full_text = ""
        for text_part in data["body_text"]:
            full_text += text_part["text"] + "\n\n"
        
        articles.append((paper_id, title, full_abstract, full_text))
        


print(sys.getsizeof(articles))
print(articles[5])
print(len(articles))
