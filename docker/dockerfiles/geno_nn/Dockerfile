FROM tensorflow/tensorflow:2.14.0-gpu-jupyter

RUN pip install \
    scipy~=1.11.3 \
    scikit-learn~=1.3.1  \
    pandas~=2.1.1 \
    pandas-plink~=2.2.9 && \
    pip cache remove *

RUN apt-get update && \
    apt-get install -y \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN wget --no-check-certificate https://github.com/precimed/simu/releases/download/v0.9.4/simu_linux && \
    chmod +x simu_linux && \
    mv simu_linux  /bin/simu

RUN wget --no-check-certificate https://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_20200616.zip && \
    unzip -j plink_linux_x86_64_20200616.zip && \
    rm -rf plink_linux_x86_64_20200616.zip && \
    mv plink /bin

RUN wget --no-check-certificate https://s3.amazonaws.com/plink2-assets/plink2_linux_x86_64_20240318.zip && \
    unzip -j plink2_linux_x86_64_20240318.zip && \
    rm -rf plink2_linux_x86_64_20240318.zip && \
    mv plink2 /bin

RUN rm -rf /tmp/*
WORKDIR /root
