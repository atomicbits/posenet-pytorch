#!/usr/bin/env bash

image="pytorch-runtime"

original_dir=$(pwd)
cd "$(dirname "$0")" # move into folder where this script is located

mkdir -p pytorch-runtime/tmp
cp ../requirements.txt pytorch-runtime/tmp/

docker rmi -f "$image"

docker build -t "$image" pytorch-runtime

rm -rf pytorch-runtime/tmp
cd "$original_dir"
