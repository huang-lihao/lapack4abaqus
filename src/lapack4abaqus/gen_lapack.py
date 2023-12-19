import os
import re
import urllib.request
import zipfile

def netlib_url(
    function: str,
):
    return f"http://www.netlib.org/cgi-bin/netlibfiles.zip?format=zip&filename=/lapack/lapack_routine/{function}.f"

def gen_lapack(
    functions: list = [],
):
    for function in functions:
        url = netlib_url(function)
        print(f"Downloading {function}.zip from {url}...")
        with urllib.request.urlopen(url) as response:
            with open(f"{function}.zip", "wb") as f:
                f.write(response.read())
        print(f"Downloaded {function}.zip from {url}.")
        print(f"Unzipping {function}.zip...")
        with zipfile.ZipFile(f"{function}.zip", "r") as zip_ref:
            zip_ref.extractall(".")
        print(f"Unzipped {function}.zip.")
        print(f"Removing {function}.zip...")
        os.remove(f"{function}.zip")
    
    
    folders = ['lapack/util', 'lapack/lapack_routine']
    out = open('lapack.f', 'w')
    files = {}
    for folder in folders:
        for f in os.listdir(folder):
            file = os.path.join(folder, f)
            files[f.strip(".f")] = file
    for file in files.values():
        with open(file, 'r') as f:
            for line in f.readlines():
                for k in files.keys():
                    if "k"+k.lower() not in line:
                        line = line.replace(k.lower(), "k"+k.lower())
                    if "K"+k.upper() not in line:
                        line = line.replace(k.upper(), "K"+k.upper())
                    pass
                out.writelines([line])
    out.close()


