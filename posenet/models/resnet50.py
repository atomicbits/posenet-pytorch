import torch
import torch.nn as nn
import onnx
import torch.nn.functional as F
import torchvision


class ResNet50(nn.Module):

    def __init__(self, model_file, output_stride=16):
        super(ResNet50, self).__init__()

        # model = torchvision.models.resnet50(pretrained=False, progress=True)
        # model.eval()

        self.features = onnx.load(model_file).graph

        # last_depth = 2048
        self.output_stride = output_stride
        # self.features = model
        # self.heatmap = nn.Conv2d(last_depth, 17, 1, 1)
        # self.offset = nn.Conv2d(last_depth, 34, 1, 1)
        # self.displacement_fwd = nn.Conv2d(last_depth, 32, 1, 1)
        # self.displacement_bwd = nn.Conv2d(last_depth, 32, 1, 1)

    def forward(self, x):
        self.features.graph.input[0]
        # self.features.graph.output[0] 0..4

        x = self.features(x)
        # heatmap = torch.sigmoid(self.heatmap(x))
        # offset = self.offset(x)
        # displacement_fwd = self.displacement_fwd(x)
        # displacement_bwd = self.displacement_bwd(x)
        # return heatmap, offset, displacement_fwd, displacement_bwd
        return x
