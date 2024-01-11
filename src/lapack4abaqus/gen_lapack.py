import os
import re
import urllib.request
import zipfile

replace_keys = {
    "stop": "call xit",
    "write( *": "write( 7",
}

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
    
    
    folders = [".\\lapack\\util\\", ".\\lapack\\lapack_routine\\"]
    out = open('lapack.f', 'w')
    files = {}
    keys = []
    print(os.listdir("."))
    print(os.listdir(".\\lapack\\"))
    for folder in folders:
        for f in os.listdir(folder):
            file = os.path.join(folder, f)
            files[f.strip(".f")] = file
            out.write(f"      include '{file}'\n")

    pattern_subroutine = re.compile(r"SUBROUTINE ([a-zA-Z0-9]+)\(")
    pattern_function = re.compile(r"FUNCTION ([a-zA-Z0-9]+)\(")
    for file in files.values():
        with open(file, 'r') as f:
            for line in f.readlines():
                for pattern in [pattern_subroutine, pattern_function]:
                    res = pattern.search(line)
                    if res:
                        span = res.span()
                        target = line[span[0]:span[1]]
                        space = target.index(" ")
                        bra = target.index("(")
                        key = target[space+1:bra]
                        if key not in keys:
                            keys.append(key)
    for file in files.values():
        lines = []
        with open(file, 'r') as f:
            for line in f.readlines():
                for k in keys:
                    line = line.replace(k.lower(), "k"+k.lower())
                    line = line.replace(k.upper(), "K"+k.upper())
                for origin, target in replace_keys.items():
                    line = line.replace(origin.lower(), target.lower())
                    line = line.replace(origin.upper(), target.upper())
                lines.append(line)
        with open(file, 'w') as f:
            f.writelines(lines)
    out.close()


