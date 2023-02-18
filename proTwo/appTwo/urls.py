from django.urls import path
from . import views

urlpatterns = [
    path('records/', views.records, name='records'),
    path('users/', views.users, name='users'),
]