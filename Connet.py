from importlib.resources import contents
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ChromeDriver로 접속, 자원 로딩시간 3초
try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome('C:\chromedriver', options=options)
    driver.implicitly_wait(3)
    driver.refresh()
except:
    print("크롬드라이버 연결 에러")

xpath = driver.find_element_by_xpath
url = "https://www.airforce.mil.kr/user/indexSub.action?codyMenuSeq=156893223&siteId=last2"
input_name = xpath('//*[@id="searchName"]')
input_yy = xpath('//*[@id="birthYear"]')
input_mm = xpath('//*[@id="birthMonth"]')
input_dd = xpath('//*[@id="birthDay"]')
submit_form = xpath('//*[@id="btnNext"]')
select_trainee = xpath(
    '//*[@id="emailPic-container"]/ul/li/input')
# 편지 쓰기
start_letter_button = xpath('//*[@id="btnNext"]')
# 인터넷 편지 쓰기
internet_letter_button = xpath(
    '//*[@id="emailPic-container"]/div[3]/span/input')
# 우편번호 검색
enter_zipcode_button = xpath(
    '//*[@id="emailPic-container"]/form/div[1]/table/tbody/tr[3]/td/div[1]/span/input')
# 어쨋든 보내기
proceed_button = xpath('//*[@id="proceed-button"]')
address_input_bar = xpath('//*[@id="keyword"]')
address_enter_button = xpath(
    '//*[@id="searchContentBox"]/div[1]/fieldset/span/input[2]')
# 장기동 반도유보라 검색

# 첫번쨰 클릭
first_address = xpath('//*[@id="roadAddrTd1"]/a')
# 상세주소 입력
detail_address_input = xpath('//*[@id="rtAddrDetail"]')
address_submit_input = xpath('//*[@id="resultData"]/div/a')
# 발신자 이름
sender_name_input = xpath('//*[@id="senderName"]')
# 관계 입력
relationship_input = xpath('//*[@id="relationship"]')
# 제목 입력(자동)
title_input = xpath('//*[@id="title"]')
# 내용 입력(자동)
content_input = xpath('//*[@id="contents"]')
# 비밀번호 입력
password_input = xpath('//*[@id="password"]')

submit_button = xpath(
    '//*[@id="emailPic-container"]/form/div[2]/span[1]/input')
# 웹페이지 불러오기


def initpage():
    driver.get(url)

# 정보 입력 & 정보 조회


def infoCheck():
    print("훈련병의 이름과 생년월일을 입력해주세요!")
    name = input("이름: ")
    yy, mm, dd = map(int, input(
        "훈련병의 생년월일을 입력해주세요!: (예시: 2022,01,25) \n").split(","))
    input_name.send_keys(name)
    input_yy.send_keys(yy)
    input_mm.send_keys(mm)
    input_dd.send_keys(dd)
    submit_form.send_keys(Keys.ENTER)
    driver.switch_to.window(driver.window_handles[-1])
    try:
        select_trainee.send_keys(Keys.ENTER)
        print("훈련병 조회가 완료되었습니다!")
    except:
        print("일치하는 정보가 없습니다!")
    return name


def getInfo():
    print("작성자의 정보를 입력해주세요!")
    print("도로명 주소를 입력해주세요! (주소 찾기: https://www.juso.go.kr/openIndexPage.do)")
    address = input("주소 입력: ")
    print("상세 주소를 입력해주세요! ")
    detail_address = input("상세주소 입력: ")
    print("발신자의 이름을 입력해주세요! ")
    sender_name = input("발신자 이름 입력: ")
    print("훈련병과의 관계를 입력해주세요! ")
    relationship = input("관계 입력: ")
    print("마지막으로 설정할 비밀번호를 입력해주세요! ")
    password = input("비밀번호 입력: ")

    return [address, detail_address, sender_name, relationship, password]


def postLetter():
