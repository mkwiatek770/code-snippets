import os

dirs = ["biorxiv_medrxiv", "comm_use_subset", "noncomm_use_subset"]

for file_ in os.listdir(f"kaggle_data/{dirs[0]}/{dirs[0]}/pdf_json"):
    print(file_)

