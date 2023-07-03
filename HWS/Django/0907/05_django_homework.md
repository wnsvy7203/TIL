# 05_Django_homework

## Django Authentication System

1. Django User model
- Django에서 기본적으로 사용하는 User 모델은 아래의 경로에서 찾아볼 수 있다.
```python
    from django.contrib.auth.models import User
```
- Django 폴더 > contrib 폴더 > auth 폴더 > models.py 파일을 클릭하고 브라우저 찾기 기능으로 `class User`로 검색
- AbstractUser 가 User 를 정의하기 위한 코드를 가지고 있는 클래스이기 때문이다.

2. Create user by ModelForm
- 새 유저를 생성하기 위해서 Django 내부에 정의된 ModelForm을 사용하려 한다. 이 때 유저 생성 form을 사용하기 위해 작성하는 import 구문을 적으시오.
```python
from django.contrib.auth.forms import UserCreationForm
```

3. Django sessions
- Django는 사용자가 로그인에 성공할 경우 (a) 테이블에 세션 데이터를 저장한다. 그리고 브라우저의 쿠키에 세션 값이 발급되는데 이 세션 값의 key 이름은 (b)다.
```
a = django_session
b = sessionid
```