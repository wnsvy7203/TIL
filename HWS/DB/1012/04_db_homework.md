# Django Model Relationship

## 1. M: N True or False

- 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고, 틀렸다면 그 이유도 함께 작성하시오.
  1. Django에서 N: 1 관계는 ForeignKeyField를 사용하고, M: N 관계는 ManyToManyField 를 사용한다.
     - `T`
  2. ManyToManyField를 설정하고 만들어지는 테이블 이름은 "_앱이름__클래스이름__지정한 필드이름_"의 형태로 만들어진다.
     - `T`
  3. ManyToManyField의 첫 번째 인자는 참조할 모델, 두 번째 인자는 related_name이 작성되는데 두 가지 모두 필수적으로 들어가야 한다.
     - `F`: related_name은 필수 인자가 아니다.



## 2. Like in templates

- 아래 빈 칸 (a)와 (b)에 들어갈 코드를 각각 작성하시오.

  ```python
  class Article(models.Model):
      ...
      user = models.ForeignKey(settings.AUTH_USER_MODLE, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
  ```

  ```html
  <!-- articles/index.html -->
  
  {% for article in articles %}
  	<p>{{ article.title }}</p>
  	<form action="{% url 'articles:likes' article.pk %}" method="POST">
      	{% csft_token %}
          {% if __(a)__ in __(b)__ %}
          	<button>좋아요 취소</button>
         	{% else}
          	<button>좋아요</button>
          {% endif %}
  	</form>
  	<span>{{ __(b)__|length }}명이 이 글을 좋아합니다.</span>
  {% endfor %}
  ```

  - (a): `request.user`
  - (b): `article.like_user.all`



## 3. Follow in views

- 모델 정보가 다음과 같을 때 빈칸 a, b, c, d, e에 들어갈 코드를 작성하시오.

  ```python
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  
  
  # Create your models here.
  class User(AbstractUser):
      followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
  ```

  ```python
  app_name = 'accounts'
  urlpatterns = [
      ...,
      path('<int:user_pk>/follow/', views.follow, name='follow'),   
  ]
  ```

  ```python
  from django.contrib.auth import get_user_model
  
  User = get_user_model()
  
  @require_POST
  def follow(request, ___(a)___):
      person = get_object_or_404(User, pk=___(a)___)
      user = request.user
      
      if user != person:
          if person.__(b)__.__(c)__(pk=user.pk).exists():
              person.__(b)__.__(d)__(user)
          else:
              person.__(b)__.__(e)__(user)
      return redirect('accounts:profile', person.username)
  ```

  - (a): `user_pk`

  - (b): `followers`
  - (c): `filter`
  - (d): `remove`
  - (e): `add`



## 4. User AttributeError

- 다음과 같은 에러 메시지가 발생하는 이유와 이를 해결하는 방법과 코드를 작성하시오.

  ![image-20221012161628993](C:\Users\wnsvy7203\AppData\Roaming\Typora\typora-user-images\image-20221012161628993.png)

  - UserCreationForm은 기본적으로 django의 default user를 참조하기 때문에, 새로 생성한 User로 Form을 새로 만들어야 해결된다.

  - forms.py를 생성하고, User를 get_user_model()이라는 함수로 가져와야 한다.

    ```python
    # accounts/forms.py
    
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm
    
    
    class CustomUserCreationForm(UserCreationForm):
        
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
    ```



## 5. related_name

- 아래의 경우 ForeignKey 혹은 ManyToManyField 에 related_name 을 필수적으로 작성해야 한다 . 그 이유를 설명하시오.

  ```python
  # articles/models.py
  from django.db import models
  from django.conf import settings
  
  
  class Article(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
  ```

  - like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성된다.
  - 하지만 이미 N: 1 관계에서 해당 매니저를 사용 중이므로, 구분이 불가능하다.
  - 따라서 user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 하는데, 일반적으로 M: N에 바꿔주는 편이다.



## 6. follow templates

- person 변수에는 view 함수에서 넘어온 유저 정보가 담겨 있고, 모델 정보가 아래와 같을 때 빈칸 a, b, c, d, e에 들어갈 알맞은 코드를 각각 작성하시오.

  ```python
  app_name = 'accounts'
  urlpatterns = [
      ...,
      path('<int:user_pk>/follow/', views.follow, name='follow'),
  ]
  ```

  ```python
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  
  
  # Create your models here.
  class User(AbstractUser):
      followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
  ```

  ```html
  <!-- accounts/profile.html -->
  <h1>{{ person.username }}'s profile'</h1>
  
  <div>
      <div>
          팔로잉: {{ __(a)__|length }}
          팔로워: {{ __(b)__|length }}
      </div>
      {% if __(c)__ != __(d)__ %}
      	<div>
          	<form action="{% url 'accounts:follow' __(e)__ %}" method="POST">
                  {% csrf_token %}
                  {% if __(c)__ in __(b)__ %}
          			<button>Unfollow</button>
         			{% else}
          			<button>Follow</button>
          		{% endif %}
              </form>
      	</div>
      {% endif %}
  </div>
  ```

  - (a): `person.followings.all`
  - (b): `person.followers.all`
  - (c): `request.user`
  - (d): `person`
  - (e): `person.pk`

