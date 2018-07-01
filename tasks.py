from invoke import task


@task
def test(ctx):
    ctx.run('pytest --cov=newio_rethinkdb')


@task
def build(ctx):
    ctx.run('rm -f dist/*')
    ctx.run('python setup.py sdist')


@task
def publish(ctx):
    build(ctx)
    ctx.run('twine upload dist/*')
