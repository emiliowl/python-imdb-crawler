import requests

initial_index = 1
base_url = 'https://www.imdb.com'
search_path = '/search/title/'
headers = {"Accept-Language": "en-US,en;q=0.5"}

#'moviemeter,asc'
#'user_rating,desc',
#'num_votes,desc',
initial_parameters = {
    'groups': 'top_1000',
    'view': 'simple',
    'sort': 'num_votes,desc',
    'start': 1,
    'ref_': 'adv_nxt'
}


def crawl(url, parms):
    website_data = get_website_data(url, parms, headers)
    print(f'website data captured, writting to disk...')
    write_data_to_disk(f'file_{parms["start"]}', website_data.text)


def build_url():
    return f'{base_url}{search_path}'


def build_parms(cursor=1):
    print(f'building parameters for cursor: {cursor}...')  
    parms = initial_parameters.copy()
    parms['start'] = cursor

    return parms

def get_website_data(url, parms, headers):
    print(f'getting website data for : {url}')
    res = requests.get(url, params=parms, headers=headers)
    print(f'website data retrieval completed for : {res.url}...')
    
    return res

    
def write_data_to_disk(filename, data):
    print(f'recording new raw data to be parsed...[{filename}]')
    with open(f'data/{filename}.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    cur_cursor_val = 1
    cur_page = 1
    url = build_url()

    while cur_cursor_val < 1000:
        parms = build_parms(cur_cursor_val)
        crawl(url, parms)
        print(f'crawler completed to cursor [{cur_cursor_val}]')
        cur_cursor_val = cur_cursor_val + 50
