#!/usr/bin/env bash

image="posenet-pytorch"

original_dir=$(pwd)
cd "$(dirname "$0")" # move into folder where this script is located

mkdir tmp
cp ../requirements.txt ./tmp/

docker rmi -f "$image"

docker build -t "$image" .

rm -rf tmp
cd "$original_dir"
