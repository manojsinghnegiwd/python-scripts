import requests
import json
from io import StringIO

print('Welcome to Tell Me About Python script')
print('You can type anything from a person name to a topic name.')
print('This script search wikipedia for the information and display it here.')
print("Let's get started ... ")
print(40*'*')

user_not_exited = True
wiki_url = 'https://en.wikipedia.org/w/api.php'

def hit_wiki_api(data):
    response = requests.get(wiki_url, params=data)

    return response.json()

def find_page_id_of_topic(topic):
    response_json = hit_wiki_api({
        'action': 'query', 'list': 'search', 'srsearch': topic, 'format':'json'
    })
    
    search_results = response_json['query']['search']
    page_id = search_results[0]['pageid']

    return page_id

def repl():
    global user_not_exited

    while user_not_exited:
        user_input = input('> ')

        if user_input == 'exit':
            user_not_exited = False
        else:
            page_id = find_page_id_of_topic(user_input)
            print('Page ID: ', page_id)
repl()
