# Static/Media

- 사전 제공되는 Django 프로젝트를 기반으로 아래 문제를 순서대로 해결하고, 해결하는데 필요한 코드를 작성하시오.



1. 스크린 샷과 달리 index 페이지에서 메인 이미지가 출력되지 않는다. 이를 해결하시오.

   ```python
   # settings.py에 구문 추가
   
   STATICFILES_DIRS = [
       BASE_DIR / 'static',
   ]
   ```

   

2. 이미지를 첨부하여 게시글을 작성해보자. 게시글은 작성되는 듯 하지만 "업로드된 이미지가 없습니다!" 라는 문구가 출력된다. 올바르게 이미지가 업로드 되어 index 페이지 각 게시글에 출력 될 수 있도록 이를 해결하시오.

   ```python
   # static_media/urls.py에 구문 추가
   urlpatterns = [
       ...
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

   ```html
   <!-- create.html에 구문 추가, enctype의 속성을 반드시 설정해야 한다. -->
   <form action="" method="POST" enctype="multipart/form-data">
   ```

   ```html
   <!-- index.html <img> 태그 바깥에 if 태그를 씌운다. -->
   {% if article.image %}
     <img src="{{ article.image.url }}" alt="{{ article.image }}">
   {% endif %}
   ```