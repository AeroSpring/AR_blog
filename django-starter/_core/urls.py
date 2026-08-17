"""
URL configuration for _core project.

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


from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from wagtail.contrib.sitemaps import Sitemap
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from a_home.views import *
from a_users.views import profile_view
from a_blog.views import *

from business_cards.bc_aframe.views import *
from business_cards.bc_babylon.views import *


# Определяем sitemap для Wagtail-страниц
sitemaps = {
    'wagtail': Sitemap,
}

urlpatterns = [
    # Business cards
    path('aframe/', include('business_cards.bc_aframe.urls')),
    path('babylon/', include('business_cards.bc_babylon.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('a_users.urls')),
    path('@<username>/', profile_view, name="profile"),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('', home_view, name="home"),
    path('blog/', include('a_blog.urls')),
    path('comments/', include('comments.urls')),
    path('pages/', include('pages.urls')),

    # Путь для генерации sitemap.xml
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # Путь для отдачи robots.txt из шаблона
    path('robots.txt', TemplateView.as_view(template_name='robots/robots.txt', content_type='text/plain')),
]

# Only used in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
