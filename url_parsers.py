from bs4 import BeautifulSoup
import json

def parser_generic(html):
    return html

def parser_abc_news(html):
    soup = BeautifulSoup(html, "lxml")
    a = soup.find("div", {'data-testid':'prism-article-body'})
    return a.get_text()

def parser_bbc_news(html):
    soup = BeautifulSoup(html, "lxml")
    script = soup.find('script', {'id':'__NEXT_DATA__'})
    obj = json.loads(script.get_text())
    page = list(obj['props']['pageProps']['page'].values())[0]
    blocks = page['contents']
    text_blocks = []
    for block in blocks:
        if block['type'] != 'text': continue
        text = '\n'.join([b['model']['text'] for b in block['model']['blocks']])
        text_blocks.append(text)

    text = '\n'.join([b for b in text_blocks])
    return text

PARSERS = {
    'abc-news': parser_abc_news,
    'bbc-news': parser_bbc_news
}

def get_parser(source_name):
    parser_func = PARSERS.get(source_name, parser_generic)
    return parser_func



if __name__ == '__main__':
    import requests
    
    
    #r = requests.get('https://abcnews.go.com/Politics/texas-democratic-rep-henry-cuellar-innocent-ahead-potential/story?id=109907581')
    r = requests.get('https://www.bbc.com/news/world-middle-east-68953413')
    html = r.text
    print(parser_bbc_news(html))


