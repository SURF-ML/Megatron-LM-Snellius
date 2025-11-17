# Downloading the Dataset
- Estimated time: 20 minutes

In this tutorial, we are using HuggingFace's [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) dataset. To limit the download time we are using the 10BT shard instead of the full dataset.

To download the dataset simply use:

```bash
sbatch download_data.job
```

As before, don't forget to edit the job file with the path of your project space:

```bash
export PROJECT_SPACE=/projects/0/prjsXXXX
```
