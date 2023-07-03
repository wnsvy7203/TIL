# Django Model Relationship

- Django Project
  - 데이터베이스 M:N 관계를 활용해 좋아요 기능을 구현하시오.

1. Model
   - 좋아요 기능 구현을 위한 모델 관계를 설정한다.
2. url & view
   - `/articles/<article_pk>/like/`
     - 로그인한 유저의 요청만 처리한다.

3. Template
   - index.html 에 좋아요 여부에 따른 결과를 보여준다.
     - 좋아요를 누른 경우 ''좋아요 취소'' 텍스트, 그렇지 않은 경우 '좋아요' 텍스트가 출력 되도록 한다.
     - 특정 글의 좋아요를 누른 전체 인원수를 출력한다.

- 결과 제출

  - 결과 사진과 views.py, models.py, index.html 코드를 마크다운에 작성해서 제출하시오.

    ![결과](C:\Users\wnsvy7203\OneDrive\바탕 화면\HWS\DB\1012\결과.png)

    ```python
    # views.py
    @require_POST
    def likes(request, article_pk):
        if request.user.is_authenticated:
            article = Article.objects.get(pk=article_pk)
    
            if article.like_users.filter(pk=request.user.pk).exists():
                article.like_users.remove(request.user)
            else:
                article.like_users.add(request.user)
            return redirect('articles:index')
        return redirect('accounts:login')
    ```

    ```python
    # models.py
    class Article(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
        title = models.CharField(max_length=10)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```

    ```html
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>Articles</h1>
      {% if request.user.is_authenticated %}
        <a href="{% url 'articles:create' %}">CREATE</a>
      {% endif %}
      <hr>
      {% for article in articles %}
        <p>
          <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
        </p>
        <p>글 번호 : {{ article.pk }}</p>
        <p>제목 : {{ article.title }}</p>
        <p>내용 : {{ article.content }}</p>
        <div>
          좋아요 개수: {{ article.like_users.all|length }}
        </div>
        <div>
          <form action="{% url 'articles:likes' article.pk %}" method="POST">
            {% csrf_token %}
            {% if request.user in article.like_users.all %}
              <input type="submit" value="좋아요 취소">
            {% else %}
              <input type="submit" value="좋아요">
            {% endif %}
          </form>
        </div>
        <a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
        <hr>
      {% endfor %}
    {% endblock content %}
    ```

    