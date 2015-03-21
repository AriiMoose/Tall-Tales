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
         ('TestGame', 'KB/', 'key_facts.kfb'):
           [1425402087.97809, 'key_facts.fbc'],
         ('TestGame', 'KB/', 'chest.krb'):
           [1426785130.839778, 'chest_bc.py'],
         ('TestGame', 'KB/', 'door.krb'):
           [1425984573.790016, 'door_bc.py'],
         ('TestGame', 'KB/', 'key.krb'):
           [1425992351.329943, 'key_bc.py'],
         ('TestGame', 'KB/', 'chest_facts.kfb'):
           [1425064646.384312, 'chest_facts.fbc'],
         ('TestGame', 'KB/', 'door_facts.kfb'):
           [1425400730.035526, 'door_facts.fbc'],
         ('TestGame', 'KB/', 'test.kfb'):
           [1424366490.914166, 'test.fbc'],
        },
        compiler_version)

