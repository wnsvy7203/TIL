# 0830 Homework

## Django Web Framework

1. MTV
    - Model, Template, View의 약자

    - Model(데이터베이스 관리) - MVC의 Model과 매칭
    - Template(인터페이스, 화면) - MVC의 View와 매칭
    - View(중심 컨트롤러) - MVC의 Controller와 매칭

    1. Model
        - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
    2. Template
        - 파일의 구조나 레이아웃 정의
        - 실제 내용을 보여주는 데 사용(presentation)
    3. View
        - HTTP 요청을 수신하고 HTTP 응답 반환
        - Model을 통해 요청을 충족시키는 데 필요한 데이터에 접근
        - 템플릿에 응답의 서식 설정을 맡긴다.

2. URL
    - `Variable Routing`은 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다.

3. Django template path
    - Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 `templates` 폴더 내부를 탐색한다.