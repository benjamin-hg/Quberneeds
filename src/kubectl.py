from external_tool import run

def delete_namespace(name):
    run('kubectl', 'delete', 'namespace', name)
