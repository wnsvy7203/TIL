

# Vue with server

1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

   - DRF Server 는 단순히 요청에 따라 데이터 및 인증을 처리하는 등의 역할만 담당할 뿐 반드시 Vue 가 Client 일 필요는 없다.
     - `T`
   - Vue DRF 가 기존에 Django 만 사용했을 때와 다른 점은 Django 의 MTV 중 Template 부분을 Vue 가 대체한 것이다.
     - `T`
   - 같은 localhost 에서 활성화 되어있는 Django 와 Vue.js 서버는 서로 제약없이 리소스를 요청하고 응답 받을 수 있다.
     - `F`: Django는 8000 포트, Vue는 8080 포트를 사용하고 있기 때문에 출처가 같지 않다고 판단한다. 따라서 서버 측에서 응답할 때 Request Header CORS 관련 설정이 필요하다.

2. Server-Client 구조의 애플리케이션에서 사용자 인증 기능을 구현하고자 한다. Client 는 Vue 그리고 Server 는 DRF 를 이용하여 구현했다고 할 때 , DRF 에서 지원하는 세션 인증 방식과 토큰 인증 방식의 차이점을 서술하시오.

   - SessionAuthentication
     - 장고의 기본 세션 백엔드를 사용한다.
     - 현재 웹사이트와 같은 세션을 공유하는 클라이언트에서 서버로 AJAX 요청을 보낼 때 적합하다.
     - AJAX 요청을 보낼 때, PUT, PATCH, POST, DELETE 등의 HTTP method로 요청을 보내기 위해서는 CSRF 토큰을 실어서 요청을 보내야 한다.
     - 인증이 성공하면 request.user를 통해 User 인스턴스를 사용할 수 있다.
   - TokenAuthentication
     - client-server 구조에 적합하다.
     - 인증을 위해서는 토큰을 HTTP Authorization 헤더에 실어서 보내야 한다.
     - 인증이 실패하면 HTTP 401 Unauthorized 응답을 반환한다.

3. DRF Server 에서 토큰 인증 방식을 이용하여 사용자 인증 기능을 구현했다고 하자. 이 때 , Client 에서 인증이 필요한 API endpoint 로 요청을 보내기 위해서는 토큰 값을 HTTP `__(a)__` request header 에 실어서 요청을 보내야 한다. `__(a)__` request header 의 이름과 특징을 작성하시오.

   - (a): `Authorization`

     - 서버의 자원에 대한 접근 제어와 인증을 위해 사용하는 요청 헤더

     - 인증 스킴을 지정하는 type와 유저 인증 정보가 담긴 credentials로 구성된다.

       ```django
       Authorization: <type> <credentials>