import pkgutil
import inspect

for loader, name, is_pkg in pkgutil.iter_modules(['MachineLearn']):
    module = loader.find_module(name).load_module(name)
    print(module)