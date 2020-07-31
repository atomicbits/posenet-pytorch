#!/usr/bin/env bash

work=$(pwd)
gpu_opts="--gpus all"
image="posenet-pytorch"

docker run $gpu_opts -it --rm -v $work:/work "$image" "$@"
