from os import listdir
from os.path import join, isdir, isfile, splitext

def get_exports(chart_path):
    result = {}

    exports_dir = join(chart_path, 'exports')
    if isdir(exports_dir):
        for file_name in listdir(exports_dir):
            path = join(exports_dir, file_name)
            if isfile(path):
                key = splitext(file_name)[0].upper()
                with open(path, 'r') as f:
                    result[key] = f.read()

    return result
