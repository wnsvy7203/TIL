# Django REST Framework

## Problem

- DRF를 활용하여 게시글 관련 REST API 서버를 구축하시오.
- 프로젝트는 my_api, 앱은 articles으로 만들어 진행한다.
- DRF 기본 템플릿을 활용하여 요청을 테스트한다.



## 1. Model

- admin 페이지 혹은 django-seed 라이브러리를 활용하여 5개의 데이터를 생성한다.

  ```python
  class Article(models.Model):
      title = models.CharField(max_length=200)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```



## 2. serializers

- ArticleListSerializer
  - 모든 게시글 정보를 반환하기 위한 ModelSerializer
  - Id, title 필드 정의
- ArticleSerializer
  - 게시글 상세 정보를 반환 및 생성하기 위한 ModelSerializer
  - 모든 필드 정의



## 3. url & views

- GET articles/
  - 모든 게시글의 id와 title 컬럼을 JSON 데이터 타입으로 응답한다.
- POST articles/
  - 검증에 성공하는 경우 새로운 게시글의 정보를 DB에 저장하고, 저장된 게시글의 정보를 응답한다.
  - 검증에 실패하는 경우 400 Bad Request 예외를 발생시킨다.
- GET articles/<article_pk>/
  - 특정 게시글의 모든 컬럼을 JSON 데이터 타입으로 응답한다.
- PUT & DELETE articles/<article_pk>/
  - PUT 요청인 경우 특정 게시글의 정보를 수정한다.
    - 검증에 성공하는 경우 수정된 게시글의 정보를 DB에 저장한다.
    - 검증에 실패할 경우 400 Bad Request 예외를 발생시킨다.
    - 수정이 완료되면 수정한 게시글의 정보를 응답한다.
  - DELETE 요청인 경우 특정 게시글을 삭제한다.
    - 삭제가 완료되면 삭제한 게시글의 id를 응답한다.



> 해당 조건을 만족하는 views.py, serializers.py 코드를 마크다운에 작성하여 제출하시오.

```python
# views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from articles import serializers

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

```python
# serializers.py

from dataclasses import field

from rest_framework import serializers

from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```



