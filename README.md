### how to run

1. build

```bash
docker build -t python-git .
```

2. run container

```bash
docker run --rm -it -v $(pwd)/app:/app python-git
```

3. run dylin (it prints the process too)

```bash
bash run.sh
```

check at the last four lines:
```bash
ML-01: /app/mypackage/tests/test_inconsistent_preprocessing.py.orig: 26: 1 args have not been transformed out of 2
ML-01: /app/mypackage/tests/test_inconsistent_preprocessing.py.orig: 65: 1 args have not been transformed out of 2
```
