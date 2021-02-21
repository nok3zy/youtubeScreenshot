# Youtube Auto Screenshot

## 문제점. Problems
```
동영상을 틀고서 스크린샷을 0.05~0.1초마다 실행해서 하려고 했으나 스크린샷의 속도가 따라오지를 못함.  
예를 들어, 0.1초 마다 스크린샷을 시도 했을 때 이론상으로 나와야하는 사진의 개수가 나오지 않음.   

There are errors in program. I intended make a program that screenshot every 0.1 sec.   
Selenium's screenshot is too slow. Theoretically, it had to take one shot in 0.1 second, but failed to catch up.
```

## 오류  Error Occur
```
1. video = browser.find_element_by_id("player-container") 에서 종종 id를 찾지 못함.
2. minute,second =map(int,duration[0].text.split(":")) 에서 종종 오류 발생
3. os.makedirs(title) 에서 폴더 이름이 같으면 오류발생함. 디렉토리에 파일이 없으면 상관없음.

1. video = browser.find_element_by_id("player-container")  >  sometimes, it can't be find id.
2. minute,second =map(int,duration[0].text.split(":"))  >  sometimes, it brings error.
3. os.makedirs(title) > if you already have folder of same title, it brings errors.
```
