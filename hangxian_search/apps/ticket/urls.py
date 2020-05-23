from django.urls import path
from . import views
# from django.shortcuts import reverse


# 设置空间名
app_name = 'ticket'
urlpatterns = [
	path('search/', views.search, name='search'),
]