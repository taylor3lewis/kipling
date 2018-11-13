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
from custom_libs.toth.acutes_filter import strip_non_text

SUBJECT = "SOBRENOMES".upper()
root_link = "http://www.tiltedlogic.org/Familia/surnames-all.php?tree="

unique = set()

if __name__ == '__main__':
    # : timestamp for data ----- #
    date = datetime.datetime.now()

    # : FILE NAME ---------------------------------------------------- #
    name_file = SUBJECT + "_" + str(date.strftime('%Y-%m-%d_%Hh%Mm%Ss'))+'.txt'
    f = open('data/'+name_file, 'w')

    try:
        soup = get_soup(root_link)
        for div in soup.find_all('div', {'class': 'titlebox'}):
            for td in div.find_all('td'):
                for span in td.find_all('span', {'class': 'normal'}):
                    for a in span.find_all('a'):
                        sn = strip_non_text(a.text.lower().encode('utf-8').strip()).split()
                        for sn_token in sn:
                            if sn_token not in unique:
                                unique.add(sn_token)
                                f.write(sn_token+'\n')
    except Exception as err:
        print err
        f.close()

    f.close()
