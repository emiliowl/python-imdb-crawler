import os
from os.path import isfile
import csv
from bs4 import BeautifulSoup

def extract_data(filename, data_writer):
    print(f'Extracting all data from [{filename}]...')
    with open(f'data/{filename}', 'r') as file:
        file_content = file.readlines()
        file_data = "".join(file_content)
        soup = BeautifulSoup(file_data, 'html.parser')

        for movie_row_elem in soup.find_all("div", class_="lister-item mode-simple"):
            content_elem = movie_row_elem.find('div', class_="lister-item-content")
            a_elem = content_elem.find_next('a')
            data_row = {
                'url': a_elem.attrs['href'],
                'description': a_elem.text
            }
            data_writer(data_row)


def parse_catalog(writer):
    all_files = os.listdir('data')
    for file in [f for f in all_files if isfile(f'data/{f}')]:
        extract_data(file, writer)


def parse_data_folder():
    print(f'New file being created...')
    with open(f'movies_source_map.csv', mode='w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['url', 'description']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        parse_catalog(writer.writerow)


if __name__ == "__main__":
    parse_data_folder()
