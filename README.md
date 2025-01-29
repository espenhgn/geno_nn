# README

Container for this and that

## Docker

```
docker build --platform=linux/amd64 -t geno_nn -f docker/docker/geno_nn/Dockerfile .
```

```
docker run --platform=linux/amd64 -it --rm -v $(pwd):/geno_nn geno_nn
```

docker run --platform=linux/amd64 -it --rm geno_nn bash

export SIMU="docker run -it --rm --platform=linux/amd64 --mount type=bind,source="$(pwd)",target=/opt tf simu"

### generate simulated data
docker run -it --rm --platform=linux/amd64 --mount type=bind,source="$(pwd)",target=/opt tf simu --qt --bfile /opt/data/hapgen/chr21 --seed 123 --causal-n 100 100 --trait1-sigsq 1 0 --trait2-sigsq 0 1 --num-components 2 --out /opt/data/simu/unique --num-traits 2

docker run -it --rm --platform=linux/amd64 --mount type=bind,source="$(pwd)",target=/opt tf simu --qt --bfile /opt/data/hapgen/chr21 --seed 123 --causal-n 100     --trait1-sigsq 1   --trait2-sigsq 1   --num-components 1 --out /opt/data/simu/shared --num-traits 2

docker run -it --rm --platform=linux/amd64 --mount type=bind,source="$(pwd)",target=/opt tf simu --qt --bfile /opt/data/hapgen/chr21 --seed 123 --causal-n 50 50 50 --trait1-sigsq 1 1 0   --trait2-sigsq 1 0 1   --num-components 3 --out /opt/data/simu/partial --num-traits 2

### convert format

docker run -it --rm --platform=linux/amd64 --mount type=bind,source="$(pwd)",target=/opt tf plink2 --bfile /opt/data/hapgen/chr21 --glm allow-no-covars --pheno /opt/data/simu/shared.pheno --pheno-name trait1 --out /opt/data/simu/shared.1

docker run -it --rm --platform=linux/amd64 --mount type=bind,source="$(pwd)",target=/opt tf plink2 --bfile /opt/data/hapgen/chr21 --glm allow-no-covars --pheno /opt/data/simu/shared.pheno --pheno-name trait2 --out /opt/data/simu/shared.2

docker run -it --rm --platform=linux/amd64 --mount type=bind,source="$(pwd)",target=/opt tf plink2 --bfile /opt/data/hapgen/chr21 --glm allow-no-covars --pheno /opt/data/simu/unique.pheno --pheno-name trait1 --out /opt/data/simu/unique.1

docker run -it --rm --platform=linux/amd64 --mount type=bind,source="$(pwd)",target=/opt tf plink2 --bfile /opt/data/hapgen/chr21 --glm allow-no-covars --pheno /opt/data/simu/unique.pheno --pheno-name trait2 --out /opt/data/simu/unique.2

docker run -it --rm --platform=linux/amd64 --mount type=bind,source="$(pwd)",target=/opt tf plink2 --bfile /opt/data/hapgen/chr21 --glm allow-no-covars --pheno /opt/data/simu/partial.pheno --pheno-name trait1 --out /opt/data/simu/partial.1

docker run -it --rm --platform=linux/amd64 --mount type=bind,source="$(pwd)",target=/opt tf plink2 --bfile /opt/data/hapgen/chr21 --glm allow-no-covars --pheno /opt/data/simu/partial.pheno --pheno-name trait2 --out /opt/data/simu/partial.2

# convert for MiXer
# singularity exec --home $PWD:/home $SIF/mixer.sif python
```
import pandas as pd
for fname, out in [('{x}.{y}.trait{y}.glm.linear'.format(x=x,y=y), '{}.{}.sumstats'.format(x,y)) for x in ['unique', 'shared', 'partial'] for y in ['1', '2']]:
    pd.read_csv(fname, delim_whitespace=True)[['ID', 'REF', 'ALT', 'OBS_CT', 'T_STAT']].rename(columns={'ID':'SNP', 'REF':'A1', 'ALT':'A2', 'OBS_CT':'N', 'T_STAT':'Z'}).to_csv(out,index=False, sep='\t')
```

## Singularity

```
singularity run --nv containers/geno_nn.sif bash
```
