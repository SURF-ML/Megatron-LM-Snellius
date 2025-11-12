#!/bin/bash
#SBATCH --nodes=1
#SBATCH --partition=rome
#SBATCH --ntasks-per-node=1
#SBATCH --time=1:00:00
#SBATCH --exclusive


CONTAINER_URL=nvcr.io/nvidia/pytorch:25.10-py3
CONTAINER_NAME=megatron-torch-2.7-nvcr.25-10.sif

# enter your project space path e.g. PROJECT_SPACE=/projects/0/prjsXXXX
# if you didn't add the path to your bashrc
# PROJECT_SPACE=

if [ -z "$PROJECT_SPACE" ]; then
  echo "Error: PROJECT_SPACE is not set. Please set the project space path in this script. Example: export PROJECT_SPACE=/projects/0/prjsXXXX"
  exit 1
fi

CONTAINER_OUTPUT_DIR=$PROJECT_SPACE/containers/

export APPTAINER_TMPDIR=/dev/shm/$USER
export APPTAINER_CACHEDIR=/scratch-shared/$USER/apptainer

mkdir -p $APPTAINER_TMPDIR $APPTAINER_CACHEDIR $CONTAINER_OUTPUT_DIR

CONTAINER_OUTPUT_PATH=$CONTAINER_OUTPUT_DIR/$CONTAINER_NAME

# Define apptainer definition file inline for more flexibility
TMP_CONTAINER_FILENAME=/dev/shm/$USER/megatron.def

cat <<EOF > $TMP_CONTAINER_FILENAME
Bootstrap: docker
From: $CONTAINER_URL

%post

     # Create the directory Triton expects and point it to the host driver
     # because Triton requires /usr/local/cuda/compat/lib/libcuda.so.1 to exist for GPU runtime
     mkdir -p /usr/local/cuda/compat/lib/
     ln -sf /usr/lib64/libcuda.so /usr/local/cuda/compat/lib/libcuda.so.1
     ln -sf libcuda.so.1 /usr/local/cuda/compat/lib/libcuda.so

     # Add this directory to the container's dynamic linker cache
     echo "/usr/local/cuda/compat/lib" > /etc/ld.so.conf.d/cuda-compat.conf
     ldconfig

     # Install dependencies
     export PIP_NO_CACHE_DIR=1
     pip install numpy==1.26.4 
     pip install huggingface_hub==0.36.0 --no-deps
     pip install transformers==4.57.1 --no-deps
     pip install tokenizers==0.22.1 --no-deps
     pip install sentencepiece==0.2.1 --no-deps
     pip install protobuf==6.33.0 --no-deps
     pip install tqdm==4.67.1 --no-deps
     pip install regex==2025.9.18 --no-deps
     pip install pyyaml==6.0.3 --no-deps
     pip install datasets==4.4.1
     pip install nltk==3.9.2 
     pip install wandb==0.22.3 

%environment
     # Prevent Python from using user site-packages from /home/<user>/.local
     export PYTHONNOUSERSITE=1
     # Prevent xalt bind
     export LD_PRELOAD=

EOF

echo "Downloading $CONTAINER_URL to $CONTAINER_OUTPUT_PATH"
apptainer build $CONTAINER_OUTPUT_PATH $TMP_CONTAINER_FILENAME

rm $TMP_CONTAINER_FILENAME
echo "Done building! Check out $CONTAINER_OUTPUT_PATH"
