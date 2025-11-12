# Downloading the Dataset
- Estimated time: 20 minutes

In this tutoria lwe are using HuggingFace's [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb). To limit the dowload time we are using the 10BT shard.
To download the dataset:

To download the dataset simply use:

```bash
sbatch download_data.job
```

As before don't forget to edit the job file with your project space path

```bash
export PROJECT_SPACE=/projects/0/prjsXXXX
```



```bash
CONTAINER=$PROJECT_SPACE/containers/megatron-torch-2.7-nvcr.25-10.sif
BIND_PATH=$PROJECT_SPACE

apptainer shell -B $BIND_PATH $CONTAINER
```

Now you are inside the root directory of the Megatron-LM container. From here you can use the pre-installed packages within the container without needing to build any virtual environments. 

```python
import os
from datasets import load_dataset

project_space = os.environ.get("PROJECT_SPACE", os.getcwd())
cache_dir = os.path.join(project_space, "my_hf_cache_dir")
output_path = os.path.join(project_space, "datasets", "FineWeb", "fineweb-10BT.jsonl")

os.makedirs(cache_dir, exist_ok=True)
os.makedirs(os.path.dirname(output_path), exist_ok=True)

shard = "sample-10BT"
dataset = load_dataset("HuggingFaceFW/fineweb", shard, cache_dir=cache_dir, split="train")
dataset.to_json(output_path)
```