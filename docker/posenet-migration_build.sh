#!/usr/bin/env bash

image="posenet-migration"

original_dir=$(pwd)
cd "$(dirname "$0")" # move into folder where this script is located

docker rmi -f "$image"

docker build -t "$image" posenet-migration

cd "$original_dir"
