from newsapi import NewsApiClient
import requests

import database
from model import generate_summary
from scheduler import Updater
import url_parsers
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
        source_name = news['source']['id']
        title = news['title']
        url = news['url']
        date = news['publishedAt']
        results.append((source_name, title, url, date))
    return results

def _format_date(date):
    date, time = date.split('T')
    time = time.split('.')[0].replace('Z', '')
    return f'{date} {time}'

def insert_last_headlines(sources=['abc-news']):
    db = database.database_instance
    top_headlines = get_top_headlines(sources)
    added = 0
    for source, title, url, date in reversed(top_headlines):
        if db.add_news(url, source, title, _format_date(date)):
            added+=1
    print(f'Added {added} new urls out of {len(top_headlines)} fetched')

    return added

def fetch_url(url):
    resp = requests.get(url)
    html = resp.text
    return html

def generate_single_summary():
    r = database.database_instance.get_last_unprocessed_url()
    if r is None: return
    r_id, url, source, title, published_date, processed_date, processed, summary = r
    html = fetch_url(url)
    text = url_parsers.parse_html(source, html)
    if text:
        summary = generate_summary(text)
    else:
        print('[ERROR] TEXT INVALID:', text, url)
    
    print(summary)
    database.database_instance.add_summary(r_id, summary)
    print('update summary for url id:', r_id)


def start_api():
    from api.flask_api import main
    main()

if __name__ == "__main__":
    # headlines_updater = Updater(insert_last_headlines, callback_args=tuple(), wait_minutes=10)
    # summaries_updater = Updater(generate_single_summary, callback_args=tuple(), wait_minutes=0.17)

    # headlines_updater.start()
    # summaries_updater.start()

    start_api()

