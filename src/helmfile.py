from external_tool import run

def charts(helmfilePath, helmArgs=None):
    args = ['helmfile','-f', helmfilePath, 'charts']
    if helmArgs:
        args += ['--args', helmArgs]

    run(*args)


def delete(helmfilePath, purge=False):
    args = ['helmfile', '-f', helmfilePath, 'delete']
    if purge:
        args += ['--purge']

    run(*args)
