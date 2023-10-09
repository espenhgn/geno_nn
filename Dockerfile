FROM tensorflow/tensorflow:2.14.0-gpu-jupyter

RUN pip install \
    scipy~=1.11.3 \
    scikit-learn~=1.3.1  \
    pandas~=2.1.1 \
    pandas-plink~=2.2.9 && \
    pip cache remove *
