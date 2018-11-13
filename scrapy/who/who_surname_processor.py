# coding: utf-8
from glob import glob
lines = []

for f in glob('data/SOBRENOME*'):
    print f
    fl = open(f, 'r')
    lines += fl.readlines()
    fl.close()

py_file = open('who.py', 'w')
py_file.write('# coding: utf-8\n')
py_file.write('SURNAMES = {')

buff = ''
unique = set()
for line in lines:
    line = line.strip('\n')
    if line not in unique:
        unique.add(line.strip('\n'))
        buff += 'u"%s":None,' % line.strip('\n')
py_file.write(buff[:-1])
py_file.write('}')
py_file.close()
