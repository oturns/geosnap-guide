import os
import time
import requests
import argparse
import subprocess
from pathlib import Path

NBS_FOLDER = "content/notebooks"
TEMPLATE_FOLDER = "./lib/template_data"


def pr(cmd):
    print(cmd)
    # os.system(cmd)
    op = subprocess.run(cmd, capture_output=True, shell=True)
    if op.stderr:
        print("\n### Log Msg. ###")
        print(op.stderr.decode())
        print("\n")
    return None


def wr(content, path):
    fo = open(path, "w")
    fo.write(content)
    fo.close()
    return None


def pull_notebooks(tgt_folder=NBS_FOLDER, tmp="./tmp"):
    """
    Download Master branch from meta package, extract notebooks and move to
    target folder
    ...

    Arguments
    ---------
    tgt_folder  : str
                  Path to target folder to put renamed notebooks
    tmp         : str
                  [Optional. Default='./tmp'] Location of temporary folder

    Returns
    -------
    None
    """
    t0 = time.time()
    # Clean start
    pr(f"rm -rf {tmp}")
    pr(f"mkdir {tmp}")
    pr(f"rm -rf {tgt_folder}")
    pr(f"mkdir {tgt_folder}")
    # Grab latest meta package
    cmd = f"git clone https://github.com/spatialucr/geosnap.git " f"{tmp}/dls/"
    pr(cmd)
    # Pre-process file names
    all_ipynbs = list(Path(f"{tmp}/dls/examples").rglob("*.ipynb"))
    for nb in all_ipynbs:
        nb = str(nb)
        if nb != nb.replace(" ", "_"):
            print(f"Renaming {nb}")
            wr(open(nb).read(), nb.replace(" ", "_"))
            nb_f = nb.replace(" ", "\ ")
            os.system(f"rm {nb_f}")
    # Copy notebooks to tgt_folder
    cmd = f"mv {tmp}/dls/examples/* {tgt_folder}/"
    pr(cmd)
    # Clean up
    pr(f"rm -rf {tmp}")
    t1 = time.time()
    print(f"\nNew notebooks collected in {round(t1-t0)} seconds")
    return None


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Pull notebooks/build book")
    parser.add_argument(
        "--pull", help="Download notebooks from federated packages", action="store_true"
    )

    args = parser.parse_args()

    if args.pull:
        _ = pull_notebooks()
