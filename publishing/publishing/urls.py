"""publishing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from publishingapp.views import *
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view()),
    path('websityReg.html', Registration.as_view()),
    path('websityAuthor.html', Author.as_view()),
    path('websityAuthor1.html', Author1.as_view()),
    path('websityChangeContract.html', ChangeContract.as_view()),
    path('websityContract.html/', Contract.as_view(), name="contract"),
    path('websityContract1.html', Contract1.as_view()),
    path('websityFormalizeContract.html', FormalizeContract.as_view()),
    path('websityPrint.html', Print.as_view()),
    path('websityPrint1.html', Print1.as_view()),
    re_path(r'websity.html', MainPage.as_view())
]
handler404 = "publishingapp.views.page_not_found_view"
