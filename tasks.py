from invoke import task


@task
def install(ctx):
    ctx.run('pip install -r requirements.txt')
    ctx.run('pre-commit install')


@task
def lint(ctx):
    ctx.run('pre-commit run --all-files')


@task
def test(ctx, cov=False, verbose=False):
    cov = ' --cov=curethinkdb --cov-report=term-missing' if cov else ''
    verbose = ' -v -x --log-level=debug' if verbose else ''
    cmd = f'pytest --tb=short{cov}{verbose} tests'
    ctx.run(cmd)


@task
def dist(ctx, upload=False):
    cmds = [
        'rm -f dist/*',
        'python setup.py bdist_wheel',
    ]
    if upload:
        cmds.append('twine upload dist/*')
    for cmd in cmds:
        ctx.run(cmd, echo=True)
