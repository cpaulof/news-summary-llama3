from newsapi import NewsApiClient

#from database import Database
#from model import generate_summary
from keys import *


client = NewsApiClient(api_key=API_KEY)

def get_sources():
    response = client.get_sources(language='en')
    if response['status'] != 'ok':
        return []
    sources = response['sources']
    sources_id = [(source['id'], source['url']) for source in sources]
    return sources_id

def get_top_headlines(sources):
    sources = ','.join(sources)
    headlines = client.get_top_headlines(sources=sources)
    results = []
    for news in headlines['articles']:
        source_name = news['source']['name']
        title = news['title']
        url = news['url']
        date = news['publishedAt']
        results.append((source_name, title, url, date))
    return results

if __name__ == "__main__":
    #print(get_sources())
    print(get_top_headlines(['bbc-news']))