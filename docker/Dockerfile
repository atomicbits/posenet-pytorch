FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime
# The default version is the CPU version!
# see: https://hub.docker.com/r/pytorch/pytorch/tags

# Install system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
      libglib2.0-0 \
      bzip2 \
      git \
      wget && \
    pip install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

COPY tmp/requirements.txt /work/

WORKDIR /work

# run pip install with the '--no-deps' argument, to avoid that tensorflowjs installs an old version of tensorflow!
# It also ensures that we know and controll the transitive dependencies (although the docker image comes
# with a lot of packages pre-installed).
RUN pip install -r requirements.txt --no-deps

# tfjs-to-tf needs tensorflow installed if you install using --no-deps
# RUN git clone https://github.com/patlevin/tfjs-to-tf.git && \
#     cd tfjs-to-tf && \
#     git checkout v0.3.0 && \
#     pip install . --no-deps && \
#     cd .. && \
#     rm -r tfjs-to-tf

ENV PYTHONPATH='/work/:$PYTHONPATH'

CMD ["bash"]
