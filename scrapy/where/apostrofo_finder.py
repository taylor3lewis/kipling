f_cities = open('LUGARES_DO_BRASIL_CITY_.txt', 'r')
unique_city = set()
for line in f_cities.readlines():
    line = line.lower().strip('\n')
    if line not in sorted(unique_city):
        unique_city.add(line)
        if '`' in line:
            print line
f_cities.close()
