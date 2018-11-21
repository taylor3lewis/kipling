f = open('como.txt', 'r')
whys = f.readlines()
f.close()

unique = set()

for w in whys:
    unique.add(w.lower().strip('\n'))

py_file = open('why.py', 'w')
py_file.write('# coding: utf-8\n')
py_file.write('COMOS = {')

buff = ''
for line in unique:
    line = line.strip('\n')
    buff += 'u"%s":None,' % line.strip('\n')
py_file.write(buff[:-1])
py_file.write('}')
py_file.close()

