# Megatron-LM on Snellius
This codebase helps Snellius users to quickly set up their LLM pretraining tasks.


A few Snellius-specific pointers:
- GPU: NVIDIA H100 SXM5 94GB (4 GPUs per node)
- Interconnect: Infiniband HDR200
- Persistent storage is provided upon grant agreement under /projects/0/prjsXXXX
- Temporary storage (/scratch-shared/$USER/) for model checkpointing and log saving
- Operating system: Red Hat Enterprise Linux 9.4 (Plow)


## Code setup
- Estimated time: 5 minutes

1. Clone the official Megatron-LM codebase in your home directory:
```bash
git clone git@github.com:NVIDIA/Megatron-LM.git
```

2. Clone this repository:
```bash
git clone git@github.com:tvosch/Megatron-LM-Snellius.git
```

Prepare the file hierarchy like and make sure by default the code is always run from the parent directory of where the Megatron-LM clone is
```
root (you are here)/
├── Megatron-LM/ ------ official Megatron-LM codebase
├── container/ -------- from Megatron-LM-Snellius
└── output/ ----------- is made automatically by Megatron-LM
launch.sh ------------- from Megatron-LM-Snellius
train-gpt.job ---------- from Megatron-LM-Snellius
```

Additionally, to smooth the installation ride and make it more generic, export your project space as environment variable:
```bash
export PROJECT_SPACE=/projects/0/prjsXXXX
```

Or add it your .bashrc to have the project space persistent so you can always change directory easy with `cd $PROJECT_SPACE`
```
echo 'export PROJECT_SPACE=/projects/0/prjsXXXX' >> ~/.bashrc
source ~/.bashrc
```

## Installation
While it is possible to follow the Megatron-LM instructions in the requirements.txt and install it within a virtual environment, we prefer to have the software stack containerized for potential performance benefits

### Apptainer (Container)
For the base container, we pull the latest NGC PyTorch container from [here](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch).

Both downloading and installing the container with additional Python packages can be done like:

```bash
sbatch container/build_container.job
```

By default, the container will be stored on your project space in the `container` folder

## Dataset


### Download
- Estimated time: 20 minutes

For the experiments, the 10BT shard from HuggingFace's [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) dataset is used. To download the dataset:
```bash
CONTAINER=$PROJECT_SPACE/containers/
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

### Tokenization/Preprocessing
- Estimated time: 30 minutes


The data is still in text format while Megatron expects pretokenized data. Thus, the preprocessing extracts given a tokenizer the token ids for the text in this step.


Assuming a CPU or GPU node is allocated via salloc:
```bash
cd <to_parent_directory_of_your_Megatron_LM_clone>
CONTAINER=$PROJECT_SPACE/containers/megatron-torch-2.7-nvcr.25-04.sif
FINEWEB_INPUT=$PROJECT_SPACE/datasets/FineWeb/fineweb-10BT.jsonl
FINEWEB_OUTPUT=$PROJECT_SPACE/datasets/FineWeb/fineweb-10BT
WORKERS=${SLURM_CPUS_PER_TASK:-16}
BIND_PATH=$PROJECT_SPACE

apptainer exec -B $BIND_PATH $CONTAINER bash -c "python Megatron-LM/tools/preprocess_data.py --input $FINEWEB_INPUT--output $FINEWEB_OUTPUT --tokenizer-type HuggingFaceTokenizer --tokenizer-model gpt2 --append-eod --log-interval 10000 --workers $WORKERS"
```

The output is an index file (idx) and the binary (bin) of the tokenizer model

## Pre-training
- Estimated time: 10 minutes to 5 days

### Sbatch
Via sbatch is preferred for a longer runs and is called like:
```bash
sbatch train-gpt.job
```



## Acknowledgments
Thanks to [@spyysalo](https://github.com/spyysalo) original LUMI Megatron-LM guide [here](https://github.com/spyysalo/lumi-fineweb-replication) which has tremendously helped this guide
