# simple_plugin
A simple class for loading and running external python files.
Useful for a plugin or command system.

## Usage

### Loading plugins
```python3
import simple_plugin

plugins = simple_plugin.Plugins('folder/of/plugins/')
```
Thats all it takes to load a folder of plugins.

### Running plugins
```python3
import simple_plugin

plugins = simple_plugin.Plugins('folder/of/plugins/')
plugins['file_name'].function()
```
Where file_name.py is a file in the folder/of/plugins/ folder.
This code will run function() from file_name.py

**note:**
The file name will have .py at the end but you don't run it with .py
Just use the name without the extension.

### Iterating over the plugins
The plugin class supports iteration.
```python3
import simple_plugin

plugins = simple_plugin.Plugins('folder/of/plugins/')
for name, ref in plugins:
    print(name)
    ref.function()
```
This will print the name of each plugin and run .function() from each plugin.
