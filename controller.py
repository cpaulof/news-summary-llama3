from newsapi import NewsApiClient

import database
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
    headlines = client.get_top_headlines(sources=sources, page_size=100)
    results = []
    for news in headlines['articles']:
        source_name = news['source']['name']
        title = news['title']
        url = news['url']
        date = news['publishedAt']
        results.append((source_name, title, url, date))
    return results

def _format_date(date):
    date, time = date.split('T')
    time = time.split('.')[0]
    return f'{date} {time}'

def insert_last_headlines(sources=['bbc-news', 'abc-news']):
    db = database.database_instance
    top_headlines = get_top_headlines(sources)
    added = 0
    for source, title, url, date in reversed(top_headlines):
        if db.add_news(url, source, title, _format_date(date)):
            added+=1
    print(f'Added {added} new urls out of {len(top_headlines)} fetched')



if __name__ == "__main__":
    #print(get_sources())
    #print(get_top_headlines(['bbc-news']))
    insert_last_headlines()