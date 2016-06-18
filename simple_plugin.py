#!/usr/bin/env python3
"""simple_plugin
A class for easily importing and calling external python files.
"""

import os
import sys


class Plugins:
    def __init__(self, folder, load_on_start=True):
        """__init__
        params:
            folder: str: The folder to load the plugins from.
            load_on_start: bool:
                True: Will load the plugins in __init__
                False: Will not load the plugins until the user calls
                       .load_plugins()
        """
        if not os.path.exists(folder):
            raise OSError('Path does not exist: {}'.format(folder))
        if not folder.endswith('/'):
            folder += '/'
        self.folder = folder
        if load_on_start:
            self.load_plugins()

    def load_plugins(self, extensions=['.py']):
        """load_plugins
        Loads the plugins from the folder specified in __init__
        params:
            extensions: list: A list of file extensions to include.
                              Defaults to .py files. It will attempt to load
                              them as a Python module no matter what file
                              extension it has.
        note: This method will temporarily move the working directory.
              It will move it back when it's done.
        """
        self.plugins = {}
        current_path = os.getcwd()
        sys.path.insert(0, self.folder)
        for name in os.listdir(self.folder):
            if (not any(name.endswith(ext) for ext in extensions) or
                    os.path.isdir(self.folder + name)):
                continue
            fname = '.'.join(name.split('.')[:-1])
            self.plugins[fname] = __import__('{}'.format(fname))
        sys.path.insert(0, current_path)
        return None

    def import_func(self, name, func):
        """import_func
        Retrieves a certain function from a plugin.
        params:
            name: str: The name of the plugin to load from.
            func: str: The name of the function to load.
        return: A reference to the function if it exists, otherwise it
                returns None.
        """
        if name in self.plugins:
            return getattr(self.plugins[name], func, None)
        return None

    def __getattr__(self, item):
        if item in self.plugins:
            return self.plugins[item]
        raise AttributeError('Plugin could not be found: "{}"'.format(item))

    def __getitem__(self, item):
        return self.__getattr__(item)

    def __iter__(self):
        for plg in self.plugins:
            yield (plg, self.plugins[plg])
        raise StopIteration
