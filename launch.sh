#!/bin/bash

# This simple launcher script sets job-specific environment variables
# and executes the provided command with python.


export MASTER_ADDR=$(scontrol show hostnames "$SLURM_STEP_NODELIST" | head -n 1)
echo "MASTER_ADDR: $MASTER_ADDR"

export MASTER_PORT=$((10000 + SLURM_JOB_ID % 50000))

export WORLD_SIZE=$SLURM_NTASKS    # Note: only valid if ntasks==ngpus
export RANK=$SLURM_PROCID
export LOCAL_RANK=$SLURM_LOCALID

python3 "$@"