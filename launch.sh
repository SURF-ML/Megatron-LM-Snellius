#!/bin/bash

# This simple launcher script sets job-specific environment variables
# and executes the provided command with python.

export RANK=$SLURM_PROCID
export LOCAL_RANK=$SLURM_LOCALID

python3 -u "$@"