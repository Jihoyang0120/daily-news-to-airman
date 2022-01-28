from Connet import *
from Crawler import *

if __name__ == "__main__":

    num_list = newsCategory()
    article_list = crawler(num_list)
    initpage()
    infoCheck(name, yy, mm, dd)
    senderInfo = getInfo()
    address, detail_address, sender_name, relationship, password = senderInfo
    for n in article_list:
        title = list(n.keys())
        article = list(n.values())
        sendLetter(address, detail_address, sender_name,
                   relationship, password, title, article)
