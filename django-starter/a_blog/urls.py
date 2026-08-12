"""
URL configuration for a_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from wagtail import urls as wagtail_urls
# from a_blog.views import *
from a_blog.views import article_search as a_blog_view

urlpatterns = [
    # path('', include(wagtail_urls)),
    path('', a_blog_view, name="blog"),
    path('', include(wagtail_urls)),
]
