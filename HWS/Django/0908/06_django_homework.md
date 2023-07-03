# 06_Django_Homework

## Django Authentication System

1. Login validation
    - 단순히 사용자가 '로그인 된 사용자인지'만을 확인하기 위하여 사용하는 속성의 이름을 작성하시오. (User 모델 내부에 정의되어 있음)

2. Login 기능 구현
    - 다음은 로그인 기능을 구현한 코드이다. 빈 칸에 들어갈 코드를 작성하시오.
    ```python
        a = AuthenticationForm
        b = login
        c = form.get_user()
    ```

3. who are you?
    - 로그인을 하지 않았을 경우 template에서 user 변수를 출력했을 때 나오는 클래스의 이름을 작성하시오.
        - AnonymousUser

4. 암호화 알고리즘
    - 제공된 공식문서를 참고하여 Django에서 기본적으로 User 객체의 password 저장에 사용하는 알고리즘, 그리고 함께 사용된 해시 함수를 찾아서 작성하시오.
        - PBKDF2 알고리즘, SHA256 함수
        - PBKDF2는 아주 가볍고 구현하기 쉬우며, SHA와 같이 검증된 해시 함수만을 사용한다.
            - PBKDF2(PRF, Password, salt, c, DLen)
                - PRF: 난수(예: HMAC)
                - Password: 패스워드
                - Salt: 암호학 솔트
                - c: 원하는 iteration 반복 수
                - DLen: 원하는 다이제스트 길이

5. Logout 기능 구현
    - 로그아웃 기능을 구현하기 위하여 다음과 같이 코드를 작성하였다. 로그아웃 기능을 실행 시 문제가 발생한다고 할 때, 그 이유와 해결 방법을 작성하시오.
        - 로그아웃의 함수와 이름이 겹친다는 문제
        ```python
        from django.contrib.auth import logout as auth_logout   # 로그아웃 함수와 이름이 겹치기 때문에 auth_logout으로 변경하여 실행하면 문제없이 처리된다.


        def logout(request):
            auth_logout(request)
            return redirect('accounts:login')
        ```
