# Django REST Framework

1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.
   - URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다.
     - `T`
   - HTTP Method는 GET과 POST 두 종류 뿐이다.
     - `F`: PUT, DELETE 역시 HTTP Method다.
   - 'https://www.fifa.com/worldcup/teams/team/43822/create/'는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.
     - `F`



2. 다음의 HTTP status code의 의미를 간략하게 작성하시오.

   - 200 `OK`: 서버가 요청을 제대로 처리했다는 뜻이다.

   - 400 `Bad Request`: 잘못된 문법을 사용하여, 서버가 요청을 이해할 수 없음을 의미한다.

   - 401 `Unauthorized`: 해당 리소스에 유효한 인증 자격 증명이 없어서 요청이 적용되지 않았음을 의미한다.
   
   - 403 `Forbidden`: 유효한 URL이고 서버에 요청이 전달되었으나, 컨텐츠에 접근할 권한이 없을 때 반환하는 오류 코드
     - 서버 자체 또는 서버에 있는 파일에 접근할 권한이 없을 경우에 발생한다. 서버에서 설정해 둔 권한과 맞지 않는 접속 요청이 들어오는 경우에 반환하는 오류 코드이다.
   - 404 `Not Found`: 클라이언트가 서버와 통신할 수는 있지만 서버가 요청한 리소스를 찾을 수 없을 경우 발생.

   - 500 `Internal Server Error`: 웹 사이트의 서버에서 문제가 발생했으나 서버가 정확한 문제가 무엇인지는 구체적으로 지정할 수 없을 때 나타내는 오류 코드



3. 아래의 모델을 바탕으로 ModelSerializer인 StudentSerializer class를 작성하시오.

   ```python
   class Student(models.Model):
       name = models.TextField()
       age = models.CharField(max_length=20)
       address = models.TextField()
   ```

   ```python
   from rest_framework import serializers
   
   from .models import Student
   
   class StudentSerializer(serializers.ModelSerializer):
       
       class Meta:
           model = Student
           fields = '__all__'
   ```



4. Serializers의 의미를 DRF 공식 문서를 참고하여 간단하게 설명하시오.
   - QuerySet 및 model Instance와 같은 복잡한 데이터를 Python 데이터 유형으로 변환한 다음, JSON, XML 또는 다른 컨텐츠 유형으로 쉽게 렌더링할 수 있다.
   - Serializers는 역직렬화(deSerialization)를 제공하여 먼저 들어오는 데이터의 유효성을 검사한 후 구문 분석된 데이터를 복합 유형으로 다시 변환할 수 있다.