FROM tensorflow/tensorflow:2.3.0

WORKDIR /work

RUN pip install tfjs-graph-converter

ENV PYTHONPATH='/work/:$PYTHONPATH'

CMD ["bash"]
