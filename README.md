# Curio + RethinkDB: Async RethinkDB driver

> Work In Progress, Not Production Ready!

## Overview

```python
from curio import run
from curethinkdb import r, set_loop_type_curio

async def main():
    conn = await r.connect('127.0.0.1', 28015)
    ret = await r.db("test").table_list().run(conn)
    print(ret)

set_loop_type_curio()
run(main)
```

## Install

```
pip install curethinkdb
```

## Document

TODO

## Need Help? Contributing?

- Open issues for any Questions/Bugs/Features
- Pull Request are welcome