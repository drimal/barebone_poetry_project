# A barebone python project using poetry

```
    poetry new -n --src <project>
    cd <project>
    poetry config virtualenvs.in-project true
    poetry env use python3.10
    source .venv/bin/activate
    poetry add black ruff pytest pre-commit
```