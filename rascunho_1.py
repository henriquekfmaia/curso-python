import glob

content_type = '# -*- coding: utf-8 -*-'
for file in glob.glob('*_teste.py'):
  with open(file, 'r') as f:
    content = f.read()
  if content_type not in content:
    content = content_type + '\n' + content
    with open(file, 'w') as f:
      f.write(content)