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
         ('TestGame', 'KB/', 'door.kfb'):
           [1424879262.251925, 'door.fbc'],
         ('TestGame', 'KB/', 'key.kfb'):
           [1424880542.069556, 'key.fbc'],
         ('TestGame', 'KB/', 'key_rules.krb'):
           [1424880542.074862, 'key_rules_fc.py'],
         ('TestGame', 'KB/', 'test.kfb'):
           [1424366490.914166, 'test.fbc'],
         ('TestGame', 'KB/', 'chest_questions.kqb'):
           [1425055035.363006, 'chest_questions.qbc'],
         ('TestGame', 'KB/', 'chest_facts.kfb'):
           [1425064646.384312, 'chest_facts.fbc'],
         ('TestGame', 'KB/', 'door_rules.krb'):
           [1425049979.659324, 'door_rules_fc.py'],
         ('TestGame', 'KB/', 'chest.krb'):
           [1425130601.642139, 'chest_bc.py'],
        },
        compiler_version)

