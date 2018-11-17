# coding: utf-8
import os
import sys
import datetime
SEPARATOR = '/'
project_path = os.path.abspath(__file__).split(SEPARATOR)
del project_path[-1]
del project_path[-1]
sys.path.append(os.path.join('/'.join(project_path), 'custom_libs'))
from custom_libs.utilities import get_soup

SUBJECT = "NOMES_MASC".upper()
root_link = "https://www.dicionariodenomesproprios.com.br/nomes-masculinos/%s/"
# SUBJECT = "NOMES_FEMI".upper()
# root_link = "https://www.dicionariodenomesproprios.com.br/nomes-femininos/%s/"

unique = set()

if __name__ == '__main__':
    # : timestamp for data ----- #
    date = datetime.datetime.now()

    # : FILE NAME ---------------------------------------------------- #
    name_file = SUBJECT + "_" + str(date.strftime('%Y-%m-%d_%Hh%Mm%Ss'))+'.txt'
    f = open(name_file, 'w')
    for i in range(1, NUMBER_OF_PAGES):
        try:
            soup = get_soup(root_link % i)
            for element in soup.find_all('ul', {'class': 'names-list'}):
                for name in element.find_all('a', {'class': 'lista-nome'}):
                    print '\r', i, name.text.lower(),
                    n = name.text.lower().encode('utf-8')
                    if n not in unique:
                        unique.add(n)
                        f.write(n+'\n')
        except Exception as err:
            print err
            f.close()
            break
    f.close()
