from django.shortcuts import render, redirect, get_object_or_404
from .models import HomePage  # импортируй свою модель HomePage


def home_view(request):
    # return render(request, 'a_home/home_page.html')
    # return render(request, 'home.html')
    # return redirect('blog/')

    # Получаем опубликованную главную страницу (предполагаем, что она одна)
    home_page = HomePage.objects.live().first()
    if not home_page:
        # Если страница не создана, можно показать заглушку
        return render(request, 'home/default_home.html', {'error': 'Главная страница не создана'})
    # Вызываем метод serve у страницы, передавая request
    return home_page.serve(request)
