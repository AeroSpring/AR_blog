from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('reviews/', views.reviews, name='reviews'),
    path('calculator/', views.calculator, name='calculator'),
]
