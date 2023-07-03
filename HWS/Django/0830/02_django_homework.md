# 0831 Homework

## Django Web Framework

1. 한국어로 번역하기
    1. Django 프로젝트를 한국어로 제공하기 위해 번역이 필요하다. 이 설정을 위해 settings.py에 어떤 변수를 어떤 값으로 할당해야 하는지 작성하시오.
    `LANGUAGE_CODE = 'ko-kr'`

    2. 추가로 settings.py에 '이 변수'가 활성화인 상태여야 1-1번 변수를 설정할 수 있다고 한다. '이 변수'는 무엇인가?
    `USE_I18N`

2. 경로 설정하기
    - 다음은 어떤 django 프로젝트의 urls.py의 모습이다. 주소'/ssafy'로 요청이 들어왔을 때 실행되는 함수가 pages 앱의 views.py 파일 안 ssafy 함수라면, 요청에 응답하기 위해 빈칸에 추가되어야 할 코드를 작성하시오.
    ```python
    from django.contrib import admin
    from django.urls import path
    from pages import views

    urlpatterns = [
        path(__(a)__),
        path('admin/', admin.site.urls),
    ]
    a = 'ssafy/', views.ssafy

3. Django Template Language
    - 아래 링크를 참고하여 각 문제들을 해결하기 위한 코드를 작성하시오.

    1. a = menu
    2. a = forloop.counter0
    3. a = empty
    4. a = if, b = else, c = endif
    5. a = length, b = title
    6. a = Y년 m월 d일 (D) A h:i

4. Form tag with Django
    1. action의 역할: form이 제출될 때 데이터를 보낼 경로 지정
    2. GET, POST
    3. HOST:PORT/create/?title=안녕하세요&content=반갑습니다&my-site=파이팅