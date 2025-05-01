from datasets import load_dataset
# download data and save it to local cache directory
dataset_path = "./.cache/hf/stanfordnlp/imdb"
dataset = load_dataset("stanfordnlp/imdb", cache_dir=dataset_path,)

#print first few)
print(dataset["train"][0:5])