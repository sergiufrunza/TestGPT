"""TestGPT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from appGPT.views import *

urlpatterns = [
    path('',MainViewHome.as_view() ,name='main_page'),
    path('register/', RegisterView.as_view(), name='register_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_page'),
    path('chat/', GPTChatView.as_view(), name='GPT_page')
]
