import requests
from bs4 import BeautifulSoup as bs

# 구독할 뉴스 입력 받기


def newsCategory():
    print("어떤 기사를 구독하시겠습니까?")
    print("사회뉴스[1], 정치뉴스[2], 경제뉴스[3], 국제뉴스[4], 문화뉴스[5], IT뉴스[6]")
    print("입력 예시: 1,2,4")
    num_list = list(map(int, input("구독할 뉴스: ").split(",")))
    return num_list

# 입력 받은 뉴스를 url주소에 들어갈 키워드로 변환


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

# 카테고리별 뉴스 크롤링


def crawler(news_list):
    article_list = []
    for news in news_list:
        keyword = Switcher(news)
        url = "https://news.daum.net/{}/#1".format(keyword)
        res = requests.get(url)
        soup = bs(res.text, 'lxml')

        # 뉴스 메인 화면에 있는 ul태크 추출
        ul = soup.find("ul", {"class": "list_mainnews"}).find("li")
        news = []
        data = ul.find("a", {"class": "link_txt"})
        # ul태크 속 li에 있는 텍스트, 주소 추출
        news.append({
            'title': data.text,
            'url': data.get("href")
        })
        # 추출한 뉴스 주소에 있는 <p> 수집
        res = requests.get(news[0]['url'])
        soup = bs(res.text, 'lxml')
        contents = soup.find("div", {"id": "harmonyContainer"}).find(
            "section").findAll("p")[:-1]
        # 수집한 <p>를 하나로 합쳐서 저장
        p_list = []
        for p in contents:
            p_text = p.text
            p_list.append(p_text)
        p_sum = "".join(p_list)
        # 게시물 최대 글자 용량에 맞게 슬라이싱
        p_sum = p_sum[0:1199]

        article = {data.text: p_sum}
        article_list.append(article)
    return article_list
