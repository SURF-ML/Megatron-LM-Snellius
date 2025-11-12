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

To run this tutorial you must clone this repository in your home directory

```bash
git clone https://github.com/SURF-ML/Megatron-LM-Snellius
```

Please ensure that you obtain the following file hierarchy:


```
root (you are here)/
├── 0_build_container/ --- build the container
├── 1_download_data/ ----- download the dataset
├── 2_tokenization/ ------ prepare the tokens
├── 3_train/ ------------- train the model
├── Megatron-LM/ --------- Megatron-LM codebase submodule
```

if the `Megatron-LM` directory is empty you can download the code following:

```bash
git submodule update --init --recursive
```

## Environment variable
- Estimated time: 5 minutes

Most of the script in the tutorial will ask you to specify the path to your project space. This path can be added in the bash file as:
```bash
export PROJECT_SPACE=/projects/0/prjsXXXX
```

You can also export this path in your .bashrc to have the project space persistent so you can always change directory easy with `cd $PROJECT_SPACE`:

```
echo 'export PROJECT_SPACE=/projects/0/prjsXXXX' >> ~/.bashrc
source ~/.bashrc
```

## Structure of the tutorial 

The tutorial consists of 4 parts:

- [Building the container](0_build_container/README.md)
- [Download the data](1_download_data/README.md)
- [Tokenization of the data](2_tokenization/README.md)
- [Train the model](3_train/README.md)



## Acknowledgments
Thanks to [@spyysalo](https://github.com/spyysalo) original LUMI Megatron-LM guide [here](https://github.com/spyysalo/lumi-fineweb-replication) which has tremendously helped this guide
