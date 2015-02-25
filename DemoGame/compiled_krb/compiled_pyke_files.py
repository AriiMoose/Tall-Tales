# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('DemoGame', 'KBs/', 'chest_facts.kfb'):
           [1424803026.447037, 'chest_facts.fbc'],
         ('DemoGame', 'KBs/', 'chest.krb'):
           [1424803026.449334, 'chest_fc.py'],
         ('DemoGame', 'KBs/', 'door.krb'):
           [1424803026.451341, 'door_fc.py'],
        },
        compiler_version)

