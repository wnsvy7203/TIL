# Debugging

- App URL mapping
  - urlpattern은 언제든지 다른 URLconf 모듈을 포함(include)할 수 있다.
  - include되는 앱의 urls.py에 urlpatterns가 작성되어 있지 않으면 에러 발생, 빈 리스트라도 작성되어 있어야 한다.

- The Django Form Class
  - form class를 forms.py에 작성하는 것이 규약은 아니고, 파일 이름이 달라도 되고 models.py에 이어붙여도 상관없지만, 유지보수의 관점에서 forms.py에 작성하는 것이 관행적으로 낫다고 본다.

- Handling HTTP requests

  - context의 들여쓰기 위치 확인

  ```python
  # articles/views.py
  
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm()
      context = {
          'form': form,
      } # form.is_valid()에서 False가 떨어지면 에러 정보가 담긴 form 인스턴스가 context로 넘어갈 수 있다.
      return render(request, 'articles/create.html', context)
  ```

- Substituting a custom User model
  - Django는 기본적인 인증 시스템과 여러 가지 필드가 포함된 User Model을 제공하고, 대부분의 개발 환경에서 기본 User Model을 Custom User Model로 대체한다.
  - AbstractUser를 상속받는 커스텀 User 클래스 작성
    - 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 된다.
  - Django는 새 프로젝트를 시작하는 경우 비록 기본 User 모델이 충분하더라도 커스텀 User 모델을 설정하는 것을 강력하게 권장한다.
    - 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문이다.

- Django의 인증 관련 built-in forms

  ```python
  from django.contrib auth import login, logout as auth_login, auth_logout
  ```

  - 로그인, 로그아웃 import 시 auth_login, auth_logout 등으로 변경해서 views.py의 함수와 충돌 방지

- 회원 가입

  ```python
  # accounts/views.py
  
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = UserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/signup.html', context)
  ```

  - 회원가입에 사용하는 UserCreationForm이 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이므로, 오류 발생

  - AuthenticationForm, SetPasswordForm, PasswordChangeForm, AdminPasswordChangeForm 등은 User 모델을 대체할 때 커스텀하지 않아도 사용 가능하다.

    - 기존 User 모델을 참조하는 Form이 아니기 때문이다.

  - 반면, UserCreationForm, UserChangeForm 등은 class Meta: model = User가 등록된 form이므로 반드시 커스텀(확장)해야 한다.

    ```python
    # accounts/forms.py
    
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm
    
    class CustomUserCreationForm(UserCreationForm):
        
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
            
    class CustomUserChangeForm(UserChangeForm):
        
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
            fields = ('email', 'first_name', 'last_name') # 수정하고자 하는 필드만 작성
    ```

- 회원 탈퇴

  - 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶다면, 탈퇴 후 로그아웃의 순서가 바뀌면 안 된다.
    - 먼저 로그아웃해버리면 해당 요청 객체 정보가 없어지므로 탈퇴에 필요한 정보 또한 없어지기 때문이다.

- 비밀번호 변경

  - 변경 후 로그인 상태가 지속되지 못하는 문제 발생

    ```python
    # accounts/views.py
    
    def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                # 현재 요청과 새 session data가 파생될 업데이트된 사용자 객체를 가져오고, session data를 적절하게 업데이트해준다.
                # 암호가 변경되어도 로그아웃되지 않도록 새로운 password의 session data로 session을 업데이트
                update_session_auth_hash(request, form.user)
                return redirect('articles:index')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/change_password.html', context)
    ```

- `@login_required` 데코레이터는 GET request method 를 처리할 수 있는 경우에만 사용

  - POST method만 허용하는 delete 등의 함수 내부에서는 `request.user.is_authenticated` 속성으로 처리

- `save() method`

  - save(commit=False)
    - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
    - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용

- User 모델 참조

  - settings.AUTH_USER_MODEL: models.py에서만 사용
  - get_user_model(): models.py 제외 다른 모든 곳에서 유저 모델 참조 시 사용

- 외래 키 데이터 누락

  ```python
  # articles/views.py
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save(commit=False)
              article.user = request.user
              article.save()
              return redirect('articles:detail', article.pk)
  ```

- 파일 또는 이미지 업로드 시에는 form 태그의 enctype 속성을 `multipart/form-data`로 변경해야 한다.

- M: N
  - `through`: 중개테이블에 추가 데이터를 사용해 다대다 관계와 연결하려는 경우에 사용
  - `symmetrical`: True일 경우 팔로우 기능을 예로 들 때, 내가 팔로우하면 상대도 나를 자동으로 팔로우하게 된다. 비대칭을 원할 경우 False로 설정