#!/usr/bin/env bash

work=$(pwd)
gpu_opts="--gpus all"
image="pytorch-runtime"

docker run $gpu_opts -it --rm -v $work:/work "$image" "$@"
