#!/usr/bin/env python

from sys import argv, exit
from deployer import Deployer
import json
import helm

if len(argv) != 3:
    print('USAGE: (install|delete) file.json')
    exit(1)

if argv[1] == "install":
    delete_mode = False
elif argv[1] == "delete":
    delete_mode = True
else:
    print('USAGE: (install|delete) file.json')
    exit(1)

with open(argv[2], 'r') as stream:
    doc = json.loads(stream.read())

if 'repositories' in doc:
    for name, url in doc['repositories'].items():
        helm.repo_add(name, url)

helm.repo_update()

deployer = Deployer()
try:
    if delete_mode:
        deployer.delete(doc['charts'], doc['env'])
    else:
        deployer.install(doc['charts'], doc['env'])
finally:
    deployer.cleanup()
