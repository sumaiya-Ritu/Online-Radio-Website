"""online_radio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from main import views as main_views
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('reply/id=<int:id>', main_views.reply, name='reply'),
    path('like-comment/', main_views.like_comment , name='like_comment'),
    path('like-reply/', main_views.like_reply , name='like_reply'),
    path('register/', account_views.register, name="register"),
    path('login/', account_views.login, name="login"),
    path('logout/', account_views.logout, name="logout")
]
