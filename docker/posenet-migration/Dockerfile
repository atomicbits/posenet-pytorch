FROM tensorflow/tensorflow:2.3.0

WORKDIR /work

RUN pip install tfjs-graph-converter
RUN pip install -U tf2onnx

ENV PYTHONPATH='/work/:$PYTHONPATH'

CMD ["bash"]
