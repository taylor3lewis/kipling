# coding: utf-8
lines_city = []

py_file = open('where.py', 'w')

py_file.write('# coding: utf-8\n')

py_file.write('MINICIPIOS = {')
f_cities = open('LUGARES_DO_BRASIL_CITY_.txt', 'r')
buff_city = ''
unique_city = set()
for line in f_cities.readlines():
    line = line.decode('utf-8').lower().strip('\n')
    if line not in sorted(unique_city):
        unique_city.add(line)
        buff_city += 'u"%s":None,' % line.lower().strip('\n')
py_file.write(buff_city[:-1].encode('utf-8'))
py_file.write('}\n')
f_cities.close()

py_file.write('ESTADOS = {')
f_states = open('LUGARES_DO_BRASIL_STATE_.txt', 'r')
buff_state = ''
unique_state = set()
for line in f_states.readlines():
    line = line.decode('utf-8').lower().strip('\n')
    if line not in sorted(unique_state):
        unique_state.add(line.strip('\n'))
        buff_state += 'u"%s":None,' % line.strip('\n')
py_file.write(buff_state[:-1].encode('utf-8'))
py_file.write('}\n')
f_states.close()

py_file.write('SIGLAS = {')
f_siglas = open('LUGARES_DO_BRASIL_SIGLAS_.txt', 'r')
buff_siglas = ''
unique_siglas = set()
for line in f_siglas.readlines():
    line = line.decode('utf-8').strip('\n')
    if line not in unique_siglas:
        unique_siglas.add(line)
        buff_siglas += 'u"%s":None,' % line.strip('\n')
py_file.write(buff_siglas[:-1].encode('utf-8'))
py_file.write('}\n')
f_siglas.close()

py_file.close()
