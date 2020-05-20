from django.shortcuts import render, redirect
from employee.models import Article
# Create your views here.
def employee_all(request):
    articles = Article.objects.all()
    return render(request, 'employee/employee_list.html', { 'articles':articles })

def new_feed(request):
    if request.method == 'POST':  # 폼이 전송되었을 때만 아래 코드를 실행
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and \
                request.POST['password'] != '':
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=request.POST['content'],
                password=request.POST['password']
            )

            # 새글 등록 끝
        return redirect(f'/employee/feed/{new_article.pk}')
    return render(request, 'employee/new_feed.html')

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'employee/detail_feed.html', {'feed': article})