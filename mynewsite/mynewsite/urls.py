"""
URL configuration for mynewsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from mainsite.views import homepage, about_page, list_page, budget_page, index, carlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/<int:id>', about_page),
    path('about/', about_page),
    path('list/', list_page),
    path('get_mybudget/<int:id>/<str:name>/<int:age>/<int:budget>', budget_page),
    path('get_mybudget', budget_page),
    path('carlist/', carlist),
    path('carlist/<int:maker>/', carlist, name='carlist-url'),
    path('<int:tvno>/', index, name='tv-url'),
    path('', index, name='tv-url'),
]
