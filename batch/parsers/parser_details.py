import os
import csv
import re
from bs4 import BeautifulSoup


def extract_data(filename, data_writer):
    print(f'Extracting all data from [{filename}]...')
    with open(f'data/details/{filename}', 'r', encoding='utf-8') as file:
        file_content = file.readlines()
        file_data = "".join(file_content)
        soup = BeautifulSoup(file_data, 'html.parser')

        data_row = dict()

        pageid_elem = soup.find("meta", property="pageId")
        data_row['url'] = f'/title/{pageid_elem.attrs["content"]}'

        for title_wrapper_elem in soup.find_all("div", class_="title_wrapper"):
            title_elem = title_wrapper_elem.find('h1')
            data_row['title'] = title_elem.text

        for movie_summary_elem in soup.find_all("div", class_="plot_summary"):
            credit_summary_item_elem_list = movie_summary_elem.find_all('div', class_="credit_summary_item")
            for credit_summary_item_elem in credit_summary_item_elem_list:
                h4_elem = credit_summary_item_elem.find('h4')
                
                if re.search('director', h4_elem.text, re.IGNORECASE):
                    a_elem = credit_summary_item_elem.find('a')
                    data_row['director'] = a_elem.text

                if re.search('stars', h4_elem.text, re.IGNORECASE):
                    a_elem_list = credit_summary_item_elem.find_all('a')
                    stars_list = ''
                    for a_elem in a_elem_list:
                        star_name = a_elem.text
                        if re.search('see full cast', a_elem.text, re.IGNORECASE):
                            break
                        
                        stars_list = f'{stars_list},{star_name}'
                    
                    data_row['stars'] = stars_list[1:]

    data_writer(data_row)


def parse_catalog(writer):
    all_files = os.listdir('data/details')
    for file in all_files:
        extract_data(file, writer)


def parse_data_folder():
    print(f'New file being created...')
    with open(f'movie_catalog.csv', mode='w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['url', 'title', 'director', 'stars']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        parse_catalog(writer.writerow)


if __name__ == "__main__":
    parse_data_folder()
