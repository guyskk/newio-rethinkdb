import functools
from newio_kernel import run
from newio_rethinkdb import ConnectionPool, r, set_loop_type

DATABASE = 'test_newio'
DB = r.db(DATABASE)


def run_it(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        set_loop_type()
        return run(f(*args, **kwargs))

    return wrapper


@run_it
async def test_table_list():
    pool = ConnectionPool(host='127.0.0.1', port=28015)
    conn = await pool.get()
    tables = await DB.table_list().run(conn)
    for table in tables:
        await DB.table_drop(table).run(conn)
    await DB.table_create('tv_shows').run(conn)
    tables = await DB.table_list().run(conn)
    assert tables == ['tv_shows']
    await pool.put(conn)
