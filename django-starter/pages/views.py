from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from .models import Review
from .models import Service
from .models import Service, CalculatorSettings
from .forms import ReviewForm
from wagtail.contrib.settings.context_processors import settings as wagtail_settings
from wagtail.models import Site


def contacts(request):
    # контакты будут доступны через контекстный процессор
    return render(request, 'pages/contacts.html')


def reviews(request):
    # Получаем параметр фильтра из GET
    rating_filter = request.GET.get('rating')
    all_reviews = Review.objects.all()
    
    # Фильтруем, если передан rating и он от 1 до 5
    if rating_filter and rating_filter.isdigit():
        rating_value = int(rating_filter)
        if 1 <= rating_value <= 5:
            all_reviews = all_reviews.filter(rating=rating_value)
    
    avg_rating = Review.objects.aggregate(Avg('rating'))['rating__avg']  # средний по всем, без фильтра
    
    form = ReviewForm()
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Ваш отзыв добавлен!")
            return redirect('pages:reviews')
    
    context = {
        'reviews': all_reviews,
        'form': form,
        'avg_rating': avg_rating,
        'current_rating': rating_filter,  # передаём текущий фильтр в шаблон
    }
    return render(request, 'pages/reviews.html', context)


def calculator(request):
    services = Service.objects.filter(is_active=True)
    # Получаем текущий сайт через Wagtail Site
    current_site = Site.find_for_request(request)
    if current_site:
        cost_per_day = CalculatorSettings.for_site(current_site).cost_per_day
    else:
        cost_per_day = 0  # или значение по умолчанию
    context = {
        'services': services,
        'cost_per_day': cost_per_day,
    }
    return render(request, 'pages/calculator.html', context)


