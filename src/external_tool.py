import sys
import subprocess

def run(*args):
    retcode = subprocess.call(args)
    if retcode != 0:
        sys.exit(retcode)
