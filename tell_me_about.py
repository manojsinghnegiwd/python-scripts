import requests
import urllib.request as urllib2
from bs4 import BeautifulSoup
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context

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

def find_url_of_page(page_id):
    response_json = hit_wiki_api({
        'action': 'query',
        'prop': 'info',
        'pageids': page_id,
        'inprop': 'url',
        'format': 'json'
    })
    search_result = response_json['query']['pages'][str(page_id)]
    return search_result['canonicalurl']

def find_page_id_of_topic(topic):
    response_json = hit_wiki_api({
        'action': 'query', 'list': 'search', 'srsearch': topic, 'format':'json'
    })
    
    search_results = response_json['query']['search']
    page_id = search_results[0]['pageid']

    return page_id

def scrap_information(url):
    wiki_page = urllib2.urlopen(url)
    parsed_wiki_page = BeautifulSoup(wiki_page, 'html.parser')
    infobox = parsed_wiki_page('table', attrs={
        'class': 'infobox'
    })
    
    if len(infobox) > 0:
        infobox_content = infobox[0].contents
        filtered_content = [tag for tag in infobox_content if tag != '\n']
        info_table = []
        for content in filtered_content:
            scope = content('th', attrs={'scope': 'row'})
            data = content('td')
            if len(scope) > 0:
                info_table.append({
                    'name': scope[0].text.strip(),
                    'data': data[0].text.strip().replace('\n', ' ')
                })
        for scope in info_table:
            print(scope['name'], ' : ', scope['data']) 

def repl():
    global user_not_exited

    while user_not_exited:
        user_input = input('> ')

        if user_input == 'exit':
            user_not_exited = False
        else:
            page_id = find_page_id_of_topic(user_input)
            page_url = find_url_of_page(page_id)
            scrap_information(page_url)
repl()
