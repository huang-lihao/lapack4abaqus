# lapack4abaqus
[![GitHub release (with filter)](https://img.shields.io/github/v/release/huang-lihao/lapack4abaqus?logo=github)
](https://github.com/huang-lihao/lapack4abaqus)
[![Upload Python Package](https://github.com/huang-lihao/lapack4abaqus/actions/workflows/python-publish.yml/badge.svg)](https://github.com/huang-lihao/lapack4abaqus/actions/workflows/python-publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/lapack4abaqus?logo=pypi)](https://pypi.org/project/lapack4abaqus/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/lapack4abaqus?logo=PyPI)](https://pypi.org/project/lapack4abaqus/)
[![GitHub License](https://img.shields.io/github/license/huang-lihao/lapack4abaqus)](https://github.com/huang-lihao/lapack4abaqus/blob/main/LICENSE)

Create `lapack.f` for Abaqus to include, by adding `k` to the name of each subroutine and function.

# Install
Use PyPI to install [lapack4abaqus](https://pypi.org/project/lapack4abaqus/):
```sh
pip install lapack4abaqus
```

# Usage
Run the following script, then you will get the desired `lapack.f` to include.
```python
from lapack4abaqus import gen_lapack

gen_lapack(
    functions = ["dgetrf", "dgetri"], # list of desired funtions or subroutines
)
```
