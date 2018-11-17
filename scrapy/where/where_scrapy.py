# coding: utf-8
import datetime
import requests
from bs4 import BeautifulSoup
from custom_libs.toth.acutes_filter import strip_non_text

SUBJECT = "lugares_do_Brasil".upper()
root_link = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"

unique_city = set()
unique_state = set()

if __name__ == '__main__':
    # : timestamp for data ----- #
    date = datetime.datetime.now()

    # : FILE NAME ---------------------------------------------------- #
    name_file1 = SUBJECT + "_CITY_.txt"  # + str(date.strftime('%Y-%m-%d_%Hh%Mm%Ss'))+'.txt'
    name_file2 = SUBJECT + "_STATE_.txt"  # + str(date.strftime('%Y-%m-%d_%Hh%Mm%Ss'))+'.txt'
    try:
        soup = BeautifulSoup(requests.get(root_link).content, 'lxml')
        cont = soup.find('div', {'id': 'mw-content-text'})
        for element in cont.find_all('tr'):
            links = element.find_all('a')
            if links:
                unique_city.add(links[0].text.lower())
                unique_state.add(links[1].text.lower())
    except Exception as err:
        print err

    f1 = open(name_file1, 'w')
    for city in sorted(unique_city):
        f1.write(city.encode('utf-8').strip() + "\n")
    f1.close()

    f2 = open(name_file2, 'w')
    for state in sorted(unique_state):
        f2.write(state.encode('utf-8').strip() + "\n")
    f2.close()
