import os
from datasets import load_dataset

# Define project space and paths
project_space = os.environ.get("PROJECT_SPACE", os.getcwd())
cache_dir = os.path.join(project_space, "my_hf_cache_dir")
output_path = os.path.join(project_space, "datasets", "FineWeb", "fineweb-10BT.jsonl")

# Create necessary directories
os.makedirs(cache_dir, exist_ok=True)
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Load and save dataset
shard = "sample-10BT"
dataset = load_dataset("HuggingFaceFW/fineweb", shard, cache_dir=cache_dir, split="train")
dataset.to_json(output_path)    