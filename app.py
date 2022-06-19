import NewsAPI

news = NewsAPI.getCountryNews('IN', 'hi')

num = 0

for news_data in news:
    num += 1
    news_data_ = news_data['news']
    print ('# - News ' + str(num) + '\n')
    print('Title: ' + news_data_['title'] + '\n')
    print('Sub-Title: ' + news_data_['subTitle'] + '\n')
    print('Link: ' + news_data_['url'] + '\n')
    print('Provider: ' + news_data_['provider'] + '\n')
