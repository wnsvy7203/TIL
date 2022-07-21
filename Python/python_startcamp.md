# Python_Startcamp

## VS code

-  `Ctrl+s`로 저장 

- `Ctrl+Shift+백틱` : 새 터미널
- `Ctrl+백틱` : 터미널 열기



## 저장

#### 변수

- 숫자
- 글자(string)
- 참/거짓(True/False) - 조건의 반복

#### 리스트(List)

- 대괄호`[]` 사용

#### 딕셔너리(Dictionary)

- 이름표를 단 여러 개의 변수를 저장할 수 있는 저장공간

- 중괄호`{}` 사용

- ```python
  phone_book = {'삼성증권':'1588-2323', '카카오뱅크':'1599-3333', 'SSAFY 사무국':'02-3429-5196'}
  print(phone_book['카카오뱅크'])
  ```



## 조건문

#### if, else 조건문

- 들여쓰기(indentation) 하지 않으면 오류

#### elif

- ```python
  dust = 120
  
  if dust>150 :
      print("매우 나쁨")
  elif dust>80 : 
      print("나쁨")
  elif dust>30 : 
      print("보통")
  else :
      print("좋음")
  ```



## 반복문

### while 문

- 횟수 제한이 없는 반복

- ```python
  n=0
  while n<4 :
      print("안녕하세요")
      n=n+1
  ```

### for 문

- 횟수 제한이 없는 반복

- ```python
  hi=range(4)
  for value in hi :
      print("안녕하세요")
  ```

##### pythontutor.com - 논리 흐름 파악

##### range(start , end , step)

- range() 사용시 데이터를 다 만들지 않고 필요할때만 만들어서 메모리에 올림(메모리를 적게 사용)



## 모듈

- 함수나 변수 등을 모아 놓은 파이썬 파일

- ```python
  import reserved word
  # 필요한 함수/변수는 불러온 예악어.(함수/변수)의 형태로 재생
  
  import random
  
  menu = ['김치찌개오므라이스', '밀면', '짜글이', '닭강정']
  
  pick=random.choice(menu)
  
  print(pick)
  ```
  
- import  : reserved word(예약어)

- import 후 함수나 변수를 불러올 때 파일명.변수명

- 요청과 응답

  - `요청(request)` - `주소(url)` : 클라이언트 ==> 서버

  - `응답(response)` - `HTML` : 클라이언트 <== 서버


- `JSON` 

## API

- Apllication Program Interface

- pip install requests