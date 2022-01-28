from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 훈련병 정보 입력
print("훈련병의 이름과 생년월일을 입력해주세요!")
name = input("이름: ")
print("훈련병의 생년월일을 입력해주세요!: (예시: 2022,01,25)")
yy, mm, dd = map(int, input("생년월일 입력: ").split(","))

# Chromedriver 연결
try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome('C:\chromedriver', options=options)
    driver.implicitly_wait(3)
    driver.refresh()
except:
    print("크롬드라이버 연결 에러")

xpath = driver.find_element_by_xpath


def initpage():
    driver.get(
        "https://www.airforce.mil.kr/user/indexSub.action?codyMenuSeq=156893223&siteId=last2")


# 입력 받은 정보 입력: 훈련병 조회

def infoCheck(name, yy, mm, dd):
    print(name, yy, mm, dd)
    input_name = xpath('//*[@id="searchName"]')
    input_yy = xpath('//*[@id="birthYear"]')
    input_mm = xpath('//*[@id="birthMonth"]')
    input_dd = xpath('//*[@id="birthDay"]')
    submit_button = xpath('//*[@id="btnNext"]')

    # "훈련병 이름" 입력
    input_name.send_keys(name)
    # "훈련병 생년월일" 입력
    input_yy.send_keys(yy)
    input_mm.send_keys(mm)
    input_dd.send_keys(dd)
    submit_button.send_keys(Keys.ENTER)
    # 새 Window로 전환
    driver.switch_to.window(driver.window_handles[-1])
    # 훈련병 선택
    select_trainee_button = xpath(
        '//*[@id="emailPic-container"]/ul/li/input')
    try:
        select_trainee_button.send_keys(Keys.ENTER)
        driver.switch_to.window(driver.window_handles[-1])
        submit_button.send_keys(Keys.ENTER)
        print("훈련병 조회가 완료되었습니다!")
    except:
        print("일치하는 정보가 없습니다!")
    return

# 발신자 정보 입력


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

# 입력 받은 정보 제출


def sendLetter(address, detail_address, sender_name,
               relationship, password, title, article):

    # 클릭(인터넷 편지 쓰기)
    internet_letter_button = xpath(
        '//*[@id="emailPic-container"]/div[3]/span/input')
    internet_letter_button.send_keys(Keys.ENTER)

    # 클릭(우편번호 검색)
    enter_zipcode_button = xpath(
        '//*[@id="emailPic-container"]/form/div[1]/table/tbody/tr[3]/td/div[1]/span/input')
    enter_zipcode_button.send_keys(Keys.ENTER)
    driver.switch_to.window(driver.window_handles[-1])  # 새창으로 전환

    # 클릭(어쨋든 보내기)
    proceed_button = xpath('//*[@id="proceed-button"]')
    proceed_button.send_keys(Keys.ENTER)

    # 클릭(도로명 주소, 검색)
    address_input_bar = xpath('//*[@id="keyword"]')
    address_input_bar.send_keys(address)

    address_enter_button = xpath(
        '//*[@id="searchContentBox"]/div[1]/fieldset/span/input[2]')
    address_enter_button.send_keys(Keys.ENTER)

    # 클릭(첫번째 주소)
    first_address = xpath('//*[@id="roadAddrTd1"]/a')
    first_address.send_keys(Keys.ENTER)

    # 상세주소 입력
    detail_address_input = xpath('//*[@id="rtAddrDetail"]')
    detail_address_input.send_keys(detail_address)
    address_submit_input = xpath('//*[@id="resultData"]/div/a')
    address_submit_input.send_keys(Keys.ENTER)
    driver.switch_to.window(driver.window_handles[0])

    # 발신자 이름 입력
    sender_name_input = xpath('//*[@id="senderName"]')
    sender_name_input.send_keys(sender_name)
    # 관계 입력
    relationship_input = xpath('//*[@id="relationship"]')
    relationship_input.send_keys(relationship)
    # 제목 입력(자동)
    title_input = xpath('//*[@id="title"]')
    title_input.send_keys(title)
    # 내용 입력(자동)
    content_input = xpath('//*[@id="contents"]')
    content_input.send_keys(article)
    # 비밀번호 입력
    password_input = xpath('//*[@id="password"]')
    password_input.send_keys(password)

    # 클릭(제출)
    submit_button = xpath(
        '//*[@id="emailPic-container"]/form/div[2]/span[1]/input')
    submit_button.send_keys(Keys.ENTER)
    # 클릭(목록으로)
    to_board_button = xpath(
        '//*[@id="emailPic-container"]/div/div/div[2]/span/input')
    to_board_button.send_keys(Keys.ENTER)

    return
