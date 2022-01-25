
import requests
from bs4 import BeautifulSoup as bs
global_url = 'https://news.daum.net/ranking/kkomkkom/news'
entertain_url = 'https://news.daum.net/ranking/kkomkkom/entertain'
sports_url = "https://news.daum.net/ranking/kkomkkom/sports"

res = requests.get(url)


def newsCategory():
    print("국제 뉴스[1], 연애 기사[2], 스포츠 기사[3] 중에서 \n 무슨 구독하시겠습니까?")
    print("입력 예시: 1,2,4")
    news_list = list(map(int, input("구독할 뉴스: ").split(",")))
    return news_list


def Switcher(number):
    if number == 1:
        return "news"
    elif number == 2:
        return "entertain"
    elif number == 3:
        return "sports"
    else:
        return


def Crawler(news_list):
    for news in news_list:
        keyword = Switcher(news)
        url = "https://news.daum.net/ranking/kkomkkom/{}".format(keyword)
