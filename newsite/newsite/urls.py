"""
URL configuration for newsite project.

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
from django.urls import path, re_path

from django.conf.urls import include
from mainsite.views import homepage, about_page, list_page, budget_page, index, carlist
import mobilemarket.views as mobile
import board.views as board

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', board.index),
    path('board/<int:pid>/<str:delete_pwd>/', board.index, name='delete-url'),
    path('board/posting/', board.post_page),
    path('board/list/', board.list_page),
    path('board/contact/', board.contact_page),
    path('board/login', board.login),
    path('board/logout', board.logout),
    path('board/userinfo', board.user_info),
    re_path(r'captcha', include('captcha.urls')),
    
    path('about/<int:id>', about_page),
    path('about/', about_page),
    path('list/', list_page),
    path('mobile/',  mobile.index),
    path('mobile/<int:id>/', mobile.detail, name='detail-url'),
    path('get_mybudget/<int:id>/<str:name>/<int:age>/<int:budget>', budget_page),
    path('get_mybudget', budget_page),
    path('carlist/', carlist),
    path('carlist/<int:maker>/', carlist, name='carlist-url'),
    path('<int:tvno>/', index, name='tv-url'),
    path('', index, name='tv-url'),
]
