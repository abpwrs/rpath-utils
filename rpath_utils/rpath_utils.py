"""Main module."""
from pathlib import Path
import subprocess

class Binary(object):
    def __init__(self, path):
        self.__path = Path(str(path))

    @property
    def rpath(self):
        pass

