import requests
from flask import Flask, redirect

app = Flask(__name__)

query = "I'm Feeling Lucky"
api_key = open("api.txt").read()
cse_id = open("cse.txt").read()

def im_feeling_lucky(query, api_key, cse_id):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query
    }

    response = requests.get(url, params=params)
    data = response.json()
    if 'items' in data:
        return data['items'][0]['link']
    else:
        return None

@app.route('/search', methods=['GET'])
def search():
    result = im_feeling_lucky(query, api_key, cse_id)
    return redirect(result)

if __name__ == '__main__':
    app.run()
