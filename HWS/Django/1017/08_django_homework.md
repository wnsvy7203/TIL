# Django REST Framework

1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.
   - JSON 포맷의 데이터로 응답하기 위해서는 반드시 DRF를 사용해야 한다.
     - `F`: DjangoResponse, HttpResponse를 사용해도 가능하다.
   - DRF가 제공하는 기본 Form을 통해서만 여러 HTTP Method를 테스트 해볼 수 있다.
     - `F`: 대표적인 예외: Postmap
   - api_view 데코레이터에 작성되지 않은 HTTP Method 요청에 대해서 "500 Internal Server Error"를 응답한다.
     - `F`: 405 Method Not Allowed Error를 응답한다.
   - Serializers는 Queryset 객체를 JSON 포맷으로 변환할 수 있는 python 데이터 타입으로 만들어준다.
     - `T`



2. REST API 디자인 가이드
   - REST API 디자인 설계 시 가장 중요한 항목을 2가지로 요약한다면, "정보의 자원을 표현해야 하는 `__(a)__`와 자원에 대한 행위를 표현하는 `__(b)__`라고 할 수 있다."
   - 빈칸 a, b에 들어갈 알맞은 답을 작성하시오.
     - (a): UTI
     - (b): HTTP Method



3. 아래에서 빈칸 a, b, c, d, e에 들어갈 코드를 작성하시오.

   - 해당 view 함수는 유효성 검사를 통과했을 경우, serializer 데이터와 http status code 201을 반환하며, 유효성 검사를 통과하지 못했을 경우 http status code 400을 반환한다.

     ```python
     from rest_framework import status
     
     @api_view(__(a)__)
     def create_article(request):
         serializer = ArticleSerializer(__(b)__)
         if serializer.is_valid(__(c)__):
             serializer.save()
             return Response(__(d)__, __(e)__)
     ```

     - (a): `['POST']`
     - (b): `request.data`
     - (c): `raise_exception=True`
     - (d): `serializer.data` 
     - (e): `status=status.HTTP_201_CREATED`