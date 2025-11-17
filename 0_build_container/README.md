# Building the Container

For the base container, we pull the latest NGC PyTorch container from [here](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch).
Both downloading and installing the container with additional Python packages can be done like:

```bash
sbatch build_container.job
```

Note that you have to edit the `build_container.job` file to export your project space:

```bash
export PROJECT_SPACE=/projects/0/prjsXXXX
```

You can leave the corresponding lines in the file commented if you have enter your path in your bashrc.
By default, the container will be stored on your project space in the `container` folder