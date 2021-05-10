import requests

parms = {
    'criteria': 'spielberg hanks'
}

res = requests.get('http://localhost:5000/api/movies/search', params=parms)
print(res.status_code)
print(res.text)
print(res.json())