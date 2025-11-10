import os
from datasets import load_dataset
from datasets import load_dataset_builder

project_space = os.environ.get("PROJECT_SPACE", os.getcwd())
cache_dir = os.path.join(project_space, "my_hf_cache_dir")
output_path = os.path.join(project_space, "datasets", "FineWeb", "fineweb-10BT.jsonl")

os.makedirs(cache_dir, exist_ok=True)
os.makedirs(os.path.dirname(output_path), exist_ok=True)

ds_name = "HuggingFaceFW/fineweb"
ds_builder = load_dataset_builder(ds_name)
print(ds_builder.info.description)
print(ds_builder.info.features)


sample = "sample-10BT"
dataset = load_dataset(ds_name, name=sample, cache_dir=cache_dir, split="train")
dataset.to_json(output_path)