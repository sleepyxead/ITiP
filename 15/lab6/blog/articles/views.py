from django.shortcuts import render, redirect
from .models import Article
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # если поля заполнены без ошибок
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = "Имя должно быть уникальным."
                    return render(request, 'create_post.html', {'form': form})
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})

    else:
        raise Http404


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        try:
            User.objects.get(username=username)
            context = {'error_message': 'Пользователь с таким именем уже есть'}
            return render(request, 'registration.html', context)
        except User.DoesNotExist:
            User.objects.create_user(username=username, password=password, email=email)
            success_message = 'Успешная регистрация'
            return render(request, 'registration.html', {'success_message': success_message})
    return render(request, 'registration.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('archive')  # Replace 'home' with the name of your home page URL pattern
        else:
            error_message = 'Такого аккаунта не существует'
            return render(request, 'authentication.html', {'error_message': error_message})

    return render(request, 'authentication.html')

def logout_view(request):
    logout(request)
    return redirect('archive')  # Replace 'home' with the name of your home page URL pattern




