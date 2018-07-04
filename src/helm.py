from os.path import join
from external_tool import run

def repo_add(name, url):
    run('helm', 'repo', 'add', name, url)


def repo_update():
    run('helm', 'repo', 'update')


def fetch(name, version, destination):
    if version:
        run('helm', 'fetch', name, '--version', version, '--untar', '--untardir', destination)
    else:
        run('helm', 'fetch', name, '--untar', '--untardir', destination)

    return join(destination, name.split('/', 2)[1]);
