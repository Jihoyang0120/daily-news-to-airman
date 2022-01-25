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

url = "https://www.airforce.mil.kr/user/indexSub.action?codyMenuSeq=156893223&siteId=last2"
input_name = driver.find_element_by_xpath('//*[@id="searchName"]')
input_yy = driver.find_element_by_xpath('//*[@id="birthYear"]')
input_mm = driver.find_element_by_xpath('//*[@id="birthMonth"]')
input_dd = driver.find_element_by_xpath('//*[@id="birthDay"]')
submit_form = driver.find_element_by_xpath('//*[@id="btnNext"]')
select_trainee = driver.find_element_by_xpath(
    '//*[@id="emailPic-container"]/ul/li/input')
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

# 해쉬태그 서칭


def connect(url):
    driver.get('https://www.mangoplate.com/search/' + url)
