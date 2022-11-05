import requests

list =[]
def news():
    api_address = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=3ba5a764fac244b48b30cac44a1b59d8'
    news = requests.get(api_address).json()

    news_article = []
    for n in range(3):
        news_article.append(news["articles"][n]['title'])
        #print(news_article)

    for i in range(3):
        list.append(news_article)
        return list