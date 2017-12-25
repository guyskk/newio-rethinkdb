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

### connect, run

Just call them as coroutine `await xxx()`.

### reql

Not Support.

### ConnectionPool

```python
from curio import run
from curethinkdb import ConnectionPool, r, set_loop_type_curio

async def main()
    pool = ConnectionPool(host='127.0.0.1', port=28015)
    conn = await pool.get()
    ret = await r.db("test").table_list().run(conn)
    await pool.put(conn)

set_loop_type_curio()
run(main)
```

## Need Help? Contributing?

- Open issues for any Questions/Bugs/Features
- Pull Requests are welcome
