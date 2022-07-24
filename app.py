import NewsAPI

news = NewsAPI.getCountryNews(
                    'IN', # country
                     'hi' # lang
                    )
# print(f"{news[n]['title']}")
print(f"{news}")
