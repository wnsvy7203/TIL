# Django REST Framework

## Problem

- DRF를 활용하여 음악 정보 관련 REST API 서버를 구축하시오.
- 프로젝트는 my_api, 앱은 music으로 만들어 진행한다.
- Postman을 활용하여 각 HTTP Method에 맞는 요청을 테스트하시오.



## 1. Model & Admin

- 작성할 모델 및 필드 정보

- admin 페이지를 활용하여 가수, 해당 가수가 부른 노래를 2개씩 작성한다.

  ```python
  class Artist(models.Model):
      name = models.CharField(max_length=200)
  
  
  class Music(models.Model):
      artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
      title = models.CharField(max_length=200)
  ```



## 2. Serializer

#### ArtistListSerializer

- 모든 가수의 정보를 반환하기 위한 Serializer
- id, name 필드 출력



#### ArtistSerializer

- 상세 가수의 정보를 생성 및 반환하기 위한 Serializer
- id, name, music_set, music_count 필드 출력(music_count 필드는 music_set을 count한 결과이다.)



#### MusicListSerializer

- 모든 음악의 정보를 반환하기 위한 Serializer
- id, title 필드 출력



#### MusicSerializer

- 상세 음악의 정보를 생성 및 반환하기 위한 Serializer
- id, title, artist 필드 출력



## 3. url & view

#### GET & POST

`api/v1/artists/`

- GET 요청인 경우 모든 가수의 id와 name 컬럼을 JSON으로 응답한다.
- POST 요청인 경우 가수의 정보를 생성한다.
  - 검증에 성공하는 경우 가수의 정보를 DB에 저장하고 생성된 가수의 정보와 201 Created를 응답한다.
  - 검증에 실패하는 경우 400 Bad Request를 응답한다.



#### Get

`api/v1/artists/<artist_pk>/`

- 특정 가수의 모든 컬럼을 JSON으로 응답한다.
- 특정 가수의 노래 정보와 노래의 개수 정보를 함께 응답한다.



#### POST

`api/v1/artists/<artist_pk>/music/`

- 특정 가수의 음악의 정보를 생성한다.
- 검증에 성공하는 경우 음악의 정보를 DB에 저장하고 생성된 음악의 정보와 201 Created를 응답한다.
- 검증에 실패하는 경우 400 Bad Request를 응답한다.



#### GET

`api/v1/music/`

- 모든 음악의 id와 title 컬럼을 JSON으로 응답한다.



#### GET & PUT & DELETE

`api/v1/music/<music_pk>/`

- GET 요청인 경우 특정 음악의 모든 컬럼을 JSON으로 응답한다.
- PUT 요청인 경우 특정 음악의 정보를 수정한다.
  - 검증에 성공하는 경우 수정된 음악의 정보를 DB에 저장한다.
  - 검증에 실패하는 경우 400 Bad Request를 응답한다.
  - 수정이 완료된 이후에 수정된 음악의 정보를 응답한다.
- DELETE 요청일 경우 특정 음악의 정보를 삭제한다.
  - 삭제가 완료된 이후에 삭제한 음악의 id와 204 No Comment를 응답한다.



## 결과 제출

- 각 요청에 해당하는 JSON 응답 결과와 views.py, serializers.py 코드를 마크다운에 작성하여 제출하시오.

  ```json
  /* http://127.0.0.1:8000/api/v1/artists/ */ - GET
  [
      {
          "id": 1,
          "name": "주호"
      },
      {
          "id": 2,
          "name": "김재환"
      },
      {
          "id": 3,
          "name": "주호"
      }
  ]
  ```

  ```json
  /* http://127.0.0.1:8000/api/v1/artists/ */ - POST
  {
      "id": 4,
      "name": "이승기"
  }
  ```

  ```json
  /* http://127.0.0.1:8000/api/v1/artists/4/ */ - GET
  {
      "id": 4,
      "music_set": [],
      "music_count": 0,
      "name": "이승기"
  }
  ```

  ```json
  /* http://127.0.0.1:8000/api/v1/artists/4/music/ */ - POST
  {
      "id": 8,
      "title": "삭"
  }
  ```

  ```json
  /* http://127.0.0.1:8000/api/v1/music/ */ - GET
  [
      {
          "id": 1,
          "title": "내가 아니라도"
      },
      {
          "id": 2,
          "title": "삭제"
      },
      {
          "id": 3,
          "title": "술도 못하는데"
      },
      {
          "id": 4,
          "title": "달팽이"
      },
      {
          "id": 5,
          "title": "술도 못하는데"
      },
      {
          "id": 6,
          "title": "바래다주던 길"
      },
      {
          "id": 7,
          "title": "되돌리다"
      },
      {
          "id": 8,
          "title": "삭"
      }
  ]
  ```

  ```json
  /* http://127.0.0.1:8000/api/v1/music/8/ */ - GET
  {
      "id": 8,
      "title": "삭"
  }
  ```

  ```json
  /* http://127.0.0.1:8000/api/v1/music/8/ */ - PUT
  {
      "id": 8,
      "title": "삭제",
      "artist": 4
  }
  ```

  ```json
  /* http://127.0.0.1:8000/api/v1/music/8/ */ - DELETE 후 GET으로 조회
  {
      "detail": "Not found."
  }
  ```

  

  ```python
  # views.py
  
  from django.shortcuts import get_list_or_404, get_object_or_404
  from rest_framework import status
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  from .models import Artist, Music
  from .serializers import (ArtistListSerializer, ArtistSerializer,
                            MusicListSerializer, MusicSerializer)
  
  
  @api_view(['GET', 'POST'])
  def artist_list(request):
      if request.method == 'GET':
          # artists = Artist.objects.all()
          artists = get_list_or_404(Artist)
          serializer = ArtistListSerializer(artists, many=True)
          return Response(serializer.data)
  
      elif request.method == 'POST':
          serializer = ArtistListSerializer(data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  
  @api_view(['GET'])
  def artist_detail(request, artist_pk):
      # artist = Artist.objects.get(pk=artist_pk)
      artist = get_object_or_404(Artist, pk=artist_pk)
      serializer = ArtistSerializer(artist)
      return Response(serializer.data)
  
  
  @api_view(['POST'])
  def music_create(request, artist_pk):
      # artist = Artist.objects.get(pk=artist_pk)
      artist = get_object_or_404(Artist, pk=artist_pk)
      serializer = MusicListSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(artist=artist)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  
  @api_view(['GET'])
  def music_list(request):
      # musics = Music.objects.all()
      musics = get_list_or_404(Music)
      serializer = MusicListSerializer(musics, many=True)
      return Response(serializer.data)
  
  
  @api_view(['GET', 'DELETE', 'PUT'])
  def music_detail(request, music_pk):
      # music = Music.objects.get(pk=music_pk)
      music = get_object_or_404(Music, pk=music_pk)
  
      if request.method == 'GET':
          serializer = MusicListSerializer(music)
          return Response(serializer.data)
  
      elif request.method == 'PUT':
          serializer = MusicSerializer(music, data=request.data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response(serializer.data)
  
      elif request.method == 'DELETE':
          music.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
  
  ```

  ```python
  # serializers.py
  
  from dataclasses import fields
  
  from rest_framework import serializers
  
  from .models import Artist, Music
  
  
  class ArtistListSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Artist
          fields = ('id', 'name',)
  
  
  class MusicListSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Music
          fields = ('id', 'title',)
  
  
  class MusicSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Music
          fields = '__all__'
          read_only_fields = ('artist',)
  
  
  class ArtistSerializer(serializers.ModelSerializer):
      music_set = MusicSerializer(many=True)
      music_count = serializers.IntegerField(source='music_set.count')
  
      class Meta:
          model = Artist
          fields = '__all__'
  
  ```

  

  

