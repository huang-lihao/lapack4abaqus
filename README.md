# lapack4abaqus
Create `lapack.f` for Abaqus to include (Add `k` to the name of each subroutine and function).

# Install
Use PyPI to install [# lapack4abaqus
](https://pypi.org/project/# lapack4abaqus
/):
```sh
pip install lapack4abaqus
```

# Usage
```python
from lapack4abaqus import gen_lapack

gen_lapack(
    functions = ["dgetrf", "dgetri"], # list of desired funtions or subroutines
)
```
