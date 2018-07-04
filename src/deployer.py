from os import environ
from os.path import join
from tempfile import mkdtemp
from shutil import rmtree
from chart_inspector import get_exports
import helm, helmfile

class Deployer:
    def __init__(self):
        self.__tempDir = mkdtemp()
    
    def cleanup(self):
        rmtree(self.__tempDir)

    def install(self, charts, environment):
        chart_paths = self.__fetch(charts)
        self.__apply_environment(chart_paths, environment)

        print("\nInstalling charts (dry-run)")
        for chart_path in chart_paths:
            self.__install(chart_path, dry_run=True)

        print("\nInstalling charts")
        for chart_path in chart_paths:
            self.__install(chart_path)

    def delete(self, charts, environment):
        chart_paths = self.__fetch(charts)
        self.__apply_environment(chart_paths, environment)

        print("\nDeleting charts")
        for chart_path in chart_paths:
            self.__delete(chart_path)

    def __fetch(self, charts):
        chart_paths = []

        for name, version in charts.items():
            print("Fetching chart " + name + "-" + version)
            chart_paths.append(helm.fetch(name, version, self.__tempDir))

        return chart_paths

    def __apply_environment(self, chart_paths, environment):
        for chart_path in chart_paths:
            self.__apply_exports(chart_path, environment) 

        for key, value in environment.items():
            environ[key] = value

    def __apply_exports(self, chart_path, environment):
        for key, value in get_exports(chart_path).items():
            if key in environment:
                environment[key] += "," + value
            else:
                environment[key] = value

    def __install(self, chart_path, dry_run=False):
        helmfile.charts(join(chart_path, 'helmfile.yaml'), helmArgs='--dry-run' if dry_run else '--wait')

    def __delete(self, chart_path):
        helmfile.delete(join(chart_path, 'helmfile.yaml'), purge=True)
