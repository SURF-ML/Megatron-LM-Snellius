import os
from datasets import load_dataset
import argparse

def download_data(shard, num_proc, download_only=False):
    # project_space = os.environ.get("PROJECT_SPACE", os.getcwd())
    project_space = "/scratch-shared/larsve/Megatron-LM-Snellius"
    cache_dir = os.path.join(project_space, "my_hf_cache_dir")
    output_path = os.path.join(project_space, "datasets", "FineWeb", f"fineweb-{shard}.jsonl")

    os.makedirs(cache_dir, exist_ok=True)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print(cache_dir)
    if num_proc is None:
        num_proc=len(os.sched_getaffinity(0))
    dataset = load_dataset("HuggingFaceFW/fineweb", f"sample-{shard}", cache_dir=cache_dir, split="train", num_proc=num_proc)
    if not download_only:
        dataset.to_json(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard", type=str, default="10BT", choices=["10BT", "100BT", "350BT"])
    parser.add_argument("--num_proc", type=int, default=None)
    parser.add_argument("--download_only", action="store_true", default=False)
    args = parser.parse_args()
    download_data(args.shard, args.num_proc, args.download_only)
