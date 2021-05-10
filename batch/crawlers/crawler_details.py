import csv
import requests


base_url = 'https://www.imdb.com'
headers = {"Accept-Language": "en-US,en;q=0.5"}

    
def write_data_to_disk(filename, data):
    print(f'recording new raw data to be parsed...[{filename}]')
    with open(f'data/details/{filename}.html', 'w', encoding='utf-8') as f:
        f.write(data)


def get_website_data(url, parms, headers):
    print(f'getting website data for : {url}')
    res = requests.get(url, params=parms, headers=headers)
    print(f'website data retrieval completed for : {res.url}...')
    
    return res


def crawl(path, parms):
    website_data = get_website_data(f'{base_url}{path}', parms, headers)
    print(f'website data captured, writting to disk...')
    write_data_to_disk(f'file_{path.replace("/", "")}', website_data.text)


if __name__ == '__main__':
    with open(f'movies_source_map.csv', mode='r', encoding='utf-8', newline='') as csv_file:
            fieldnames = ['url', 'description']
            reader = csv.DictReader(csv_file, fieldnames=fieldnames)
            line_count = 0
            for row in reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'processing record: [{row["description"]}]...')
                    crawl(row['url'], {})
                    line_count += 1
                    print(f'Processed {line_count} lines.')
