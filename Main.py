from Connet import *
from Crawler import *

if __name__ == "__main__":

    num_list = newsCategory()
    article_list = crawler(num_list)
    initpage()
    infoCheck(name, yy, mm, dd)
    senderInfo = getInfo()
    address, detail_address, sender_name, relationship, password = senderInfo
    for article in article_list:
        # dict(article)의 key와 value를 인자로 사용할 수 있게 리스트로 변환
        # (dict key, value를 추출시 {type: dict.keys(), dict.values()}.)
        title = list(article.keys())
        article = list(article.values())
        sendLetter(address, detail_address, sender_name,
                   relationship, password, title, article)
