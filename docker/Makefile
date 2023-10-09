all: geno_nn.sif  # additional .sif files may be listed here for corresponding dockerfiles

%.sif: dockerfiles/%/Dockerfile
	docker build -t $* -f dockerfiles/$*/Dockerfile . && \
	scripts/convert_docker_image_to_singularity.sh $* && \
	scripts/move_singularity_file.sh $*

# Example commands executed by this make file
# 
# Run "make geno_nn.sif" will trigger this:
# docker build -t geno_nn -f dockerfiles/geno_nn/Dockerfile . && \  # build docker container
#     scripts/convert_docker_image_to_singularity.sh geno_nn && \         # produces geno_nn.sif
#     scripts/move_singularity_file.sh geno_nn        # moves geno_nn.sif to ../containers/.
#  
# Run "make all" will build all singularity containers in this project
