import argparse
import os
import converter.config as config
import converter.tfjs2tf as tfjs2tf

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='resnet50')  # mobilenet resnet50
parser.add_argument('--stride', type=int, default=16)  # 8, 16, 32 (max 16 for mobilenet)
parser.add_argument('--quant_bytes', type=int, default=4)  # 4 = float
parser.add_argument('--multiplier', type=float, default=1.0)  # only for mobilenet
parser.add_argument('--notxt', action='store_true')
args = parser.parse_args()


def main():

    model = args.model  # mobilenet resnet50
    stride = args.stride  # 8, 16, 32 (max 16 for mobilenet, min 16 for resnet50)
    quant_bytes = args.quant_bytes  # float
    multiplier = args.multiplier  # only for mobilenet

    if model == config.RESNET50_MODEL:
        model_cfg = config.bodypix_resnet50_config(stride, quant_bytes)
        print('Loading ResNet50 model')
    else:
        model_cfg = config.bodypix_mobilenet_config(stride, quant_bytes, multiplier)
        print('Loading MobileNet model')

    model_path = model_cfg['tf_dir']
    if not os.path.exists(model_path):
        print('Cannot find tf model path %s, converting from tfjs...' % model_path)
        tfjs2tf.convert(model_cfg)
        assert os.path.exists(model_path)

    return


if __name__ == "__main__":
    main()
