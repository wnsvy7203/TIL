from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm


# Create your views here.
# GET인 경우에만 함수 실행하도록 한다.
# 405 Method Not Allowed: 요청 방법이 서버에 전달되었지만 사용 불가능한 상태
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)    # data=request.POST에서 data 생략되어 있음
        if form.is_valid():                 # 유효성 검증 과정 추가
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

    # 사용자의 데이터를 받아서
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # # DB에 저장
    # # 1
    # # article = Article()
    # # article.title = title
    # # article.content = content
    # # article.save()

    # # 2
    # article = Article(title=title, content=content)
    # article.save()

    # # 3
    # # Article.objects.create(title=title, content=content)

    # # return render(request, 'articles/index.html')
    # # return redirect('/articles/')
    # # return redirect('articles:index')
    # return redirect('articles:detail', article.pk)


@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
    # return redirect('articles:detail', article.pk)


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        form = ArticleForm(request.POST, instance=article)
        # data는 생략할 수 있지만, instance는 생략할 수 없다.
        # 부모함수에 규정되어 있기를, 첫 번째 인자가 data이므로 생략 가능, 두 번째 인자는 files이므로 instance를 생략하면 files로 인식하기 때문
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
        # form.is_valid()가 false인 경우 이어질 코드가 없으므로, indentation 주의
    else:
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    # article.save()
    # return redirect('articles:detail', article.pk)
    return render(request, 'articles/update.html', context)