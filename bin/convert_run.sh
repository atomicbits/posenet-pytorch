#!/usr/bin/env bash

model=resnet50
stride=16
quant_bytes=4

./bin/posenet-migration_run.sh python convert.py --model $model --stride $stride --quant_bytes $quant_bytes

model_folder="$model"
if [ "$quant_bytes" ]; then
  model_folder="${model_folder}_float" # quant bytes 4 => '_float'; other x => '_quantx'
fi

source_folder="_tf_models/posenet/${model_folder}/stride${stride}"
target_folder="_onnx_models/posenet/${model_folder}/stride${stride}"

./bin/posenet-migration_run.sh python -m tf2onnx.convert --saved-model "$source_folder" --opset 12 --output "${target_folder}/model.onnx"
