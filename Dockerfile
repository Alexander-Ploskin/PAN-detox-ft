FROM nvidia/cuda:12.1.0-devel-ubuntu22.04

# Install system dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip \
    git \
    tmux \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/

# Install Jupyter and enable extensions
RUN pip3 install jupyter

COPY finetune /app/

RUN pip3 install -r requirements.txt

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--ServerApp.token=''", "--ServerApp.password=''"]
