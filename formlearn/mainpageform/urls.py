from django.conf.urls import url, include
from django.contrib import admin
from mainpageform import views


urlpatterns = [
    url(r'^main/', views.mainpageform , name = 'main'),
]
