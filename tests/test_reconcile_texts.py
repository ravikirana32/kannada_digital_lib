import importlib.util
from pathlib import Path
p=Path('scripts/reconcile_texts.py')
spec=importlib.util.spec_from_file_location('r',p)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
assert m.compare('ಅ ಆ','ಅ ಆ')['class']=='exact'
assert m.compare('ಅ ಆ','ಅ  ಆ')['class']=='exact'
print('OK')
