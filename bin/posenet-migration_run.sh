#!/usr/bin/env bash

work=$(pwd)
image="posenet-migration"

docker run -it --rm -v $work:/work "$image" "$@"
