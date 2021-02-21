from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import sys
from time import sleep
import os


# skip AD function.
def skip_fun():    
    sleep(6)
    skip = browser.find_elements_by_class_name("ytp-ad-skip-button")
    
    try: 
        skip[0].click()
    except:
        sleep(second-6)


title = input("title : ").rstrip()
url = input("url : ").rstrip()
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url) 

video = browser.find_element_by_id("player-container")
video.click()

duration=browser.find_elements_by_class_name("ytp-time-duration")
second = int(duration[0].text[2:])

skip_fun()

minute = 0
second = 0

while True:
    duration=browser.find_elements_by_class_name("ytp-time-duration")
    print(duration[0].text)
    minute,second =map(int,duration[0].text.split(":"))
    print(minute,second)
    if minute >= 1:
        break    
    skip_fun()

duration_sec = int(minute)*60 + int(second)
print(duration_sec)

try:
    os.makedirs(title)
except:
    pass
    # 가능한 새로 만들어라. 오류난다.
    # title = "plz_choose_another_title"
    # os.makedirs("plz_choose_another_title")

print(duration_sec*10)
i=0
while True:
    i+=1
    video.screenshot(f"{title}/{i}.png")
    sleep(.05) # change speed
    



# ytp-ad-player-overlay-instream-info # 광고 유무 판단 요소
# ytp-ad-skip-button # 광고 스킵 버튼
