import requests
from bs4 import BeautifulSoup as bs


def newsCategory():
    print("어떤 기사를 구독하시겠습니까?")
    print("사회뉴스[1], 정치뉴스[2], 경제뉴스[3], 국제뉴스[4], 문화뉴스[5], IT뉴스[6]")
    print("입력 예시: 1,2,4")
    num_list = list(map(int, input("구독할 뉴스: ").split(",")))
    print(num_list)
    return num_list


def Switcher(number):
    if number == 1:
        return "society"
    elif number == 2:
        return "politics"
    elif number == 3:
        return "economic"
    elif number == 4:
        return "foreign"
    elif number == 5:
        return "culture"
    elif number == 6:
        return "digital"


def crawler(news_list):
    article_list = []
    for news in news_list:
        keyword = Switcher(news)
        url = "https://news.daum.net/{}/#1".format(keyword)
        res = requests.get(url)

        soup = bs(res.text, 'lxml')
        ul = soup.find("ul", {"class": "list_mainnews"}).find("li")

        news = []
        data = ul.find("a", {"class": "link_txt"})
        news.append({
            'title': data.text,
            'url': data.get("href")
        })

        res = requests.get(news[0]['url'])
        soup = bs(res.text, 'lxml')
        contents = soup.find("div", {"id": "harmonyContainer"}).find(
            "section").findAll("p")[:-1]

        p_list = []
        for p in contents:
            p_text = p.text
            p_list.append(p_text)

        p_sum = "".join(p_list)
        p_sum = p_sum[0:1199]

        article = {data.text: p_sum}
        article_list.append(article)
    return article_list
