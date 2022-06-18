import requests
from bs4 import BeautifulSoup

newsapi = requests.Session()

def getCountryNews(country, language):

    key = f'https://news.google.com/topstories?hl={language}-{country}&gl={country}&ceid={country}:{language}'

    news = newsapi.get(key).text
    news = BeautifulSoup(news, 'html.parser')
    
    headlines = []
    num = 0

    for i in news.find_all('div'):
        num += 1
        if num == 1:
            if '"gKDw6b"' in str(i):
                data = i.find_all('article')
                if data:
                    if data[0]:
                        heading = data[0].text
                        
                        # mainlink = i.find('a').get('href')
                        # mainlink = f'https://news.google.com/{mainlink.replace("./", "")}'

                        link = data[1].text
                        link_href = str(data[1].find_all('a')[0].get('href'))
                        link_href = f'https://news.google.com/{link_href.replace("./", "")}'

                        newspapername = data[2].find_all('div')[0].find_all('div')[0].find_all('a')[0].text
                        news_time = data[2].find_all('div')[0].find_all('div')[0].find('time').text

                        headlines.append([heading, link, link_href, newspapername, news_time])
        if num >= 9:
            num = 0
    return headlines

