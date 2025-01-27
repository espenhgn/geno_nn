FROM tensorflow/tensorflow:2.16.2-gpu-jupyter

RUN apt-get update && \
    apt-get install -y \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -U --upgrade-strategy only-if-needed \
    scipy~=1.15.1 \
    scikit-learn~=1.6.1  \
    pandas~=2.2.3 \
    pandas-plink~=2.3.1 \
    seaborn~=0.13.2 \
    statsmodels~=0.14.4 \
    lightgbm~=4.5.0 \
    h5py~=3.12.1 \
    tables~=3.10.2 \
    keras_hub~=0.18.1 \
    tensorflow~=2.16.2 \
    transformers~=4.48.1 \
    && \
    pip cache remove *

WORKDIR /tmp
RUN wget --no-check-certificate https://github.com/precimed/simu/releases/download/v0.9.4/simu_linux && \
    chmod +x simu_linux && \
    mv simu_linux  /bin/simu

RUN wget --no-check-certificate https://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_20241022.zip && \
    unzip -j plink_linux_x86_64_20241022.zip && \
    rm -rf plink_linux_x86_64_20241022.zip && \
    mv plink /bin

RUN wget --no-check-certificate https://s3.amazonaws.com/plink2-assets/alpha6/plink2_linux_x86_64_20241222.zip && \
    unzip -j plink2_linux_x86_64_20241222.zip && \
    rm -rf plink2_linux_x86_64_20241222.zip && \
    mv plink2 /bin

RUN rm -rf /tmp/*
WORKDIR /root
