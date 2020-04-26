from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('indext/', views.indexTemplate),
    path('bank/list/', views.findBanks),
]
