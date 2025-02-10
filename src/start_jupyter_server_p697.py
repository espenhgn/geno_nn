import os
import subprocess

if __name__ == '__main__':
    os.environ.update(dict(
        SIF='/ess/p697/data/durable/s3-api/espehage-nird/geno_nn/containers/geno_nn_latest.sif',
    ))
    os.environ.update(dict(
        # APPTAINER_BIND=f'{os.environ["REFERENCE"]}:/REF'
    ))

    # Executables in containers
    SIF = os.environ['SIF']
    PWD = os.getcwd()
    os.environ.update(
        dict(
            APPTAINERENV_JUPYTER_RUNTIME_DIR='/tmp',
            JUPYTER_SERVER=f"apptainer exec --nv --home={PWD}:/home --cleanenv {SIF} jupyter-server --port 8891"
        ))

    subprocess.run(os.environ['JUPYTER_SERVER'], shell=True)
