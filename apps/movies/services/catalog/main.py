import csv
import re

data = list()
director_index = dict()
stars_index = dict()


def feed_index(data_index, row_data, star_key):
    if (data_index.get(star_key, None)):
        data_index[star_key].append(row_data)
    else:
        data_index[star_key] = [row_data]


def load_data_dimensions(row_data):
    data.append(row_data)

    #preparing director dimension index
    director_key = row_data['director']
    feed_index(director_index, row_data, director_key)

    #preparing stars dimension index
    stars = row_data['stars']
    if (',' in stars):
        for star_key in stars.split(sep=','):
            feed_index(stars_index, row_data, star_key)
    else:
        feed_index(stars_index, row_data, stars)


def calculate_statistics():
    print('Total records loaded in memory:')
    print(len(data))

    print('Total records loaded in directors index:')
    print(len(director_index))

    print('Total records loaded in stars index:')
    print(len(stars_index))


def search_in_index(parameter, index):
    pattern = parameter
    r = re.compile(f'.*{pattern}.*', re.IGNORECASE)
    keys = list(filter(r.match, index.keys()))
    response = []
    for key in keys:
        response += index[key]
    
    return response #not found

def emulate_lookup():
    search_parameter = 'spielberg'
    titles_list_1 = search_in_index(search_parameter, director_index)
    titles_list_1 = list(map(lambda movie: movie["title"] ,titles_list_1))
    print('director lookup result')
    print(titles_list_1)

    search_parameter_2 = 'hanks'
    titles_list_2 = search_in_index(search_parameter_2, stars_index)
    titles_list_2 = list(map(lambda movie: movie["title"] ,titles_list_2))
    print('star lookup result')
    print(titles_list_2)

    print('final result (intersection):')
    print(list(set.intersection(set(titles_list_1), set(titles_list_2))))


def load():
    with open(f'movie_catalog.csv', mode='r', encoding='utf-8', newline='') as csv_file:
            fieldnames = ['url', 'title', 'director', 'stars']
            reader = csv.DictReader(csv_file, fieldnames=fieldnames)
            line_count = 0
            for row in reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'processing record: [{row["title"]}]...')
                    load_data_dimensions(row)
                    line_count += 1
                    print(f'Processed {line_count} lines.')

if __name__ == '__main__':
    load() 
    calculate_statistics()
    emulate_lookup()
