from django.urls import path

from . import views

app_name = 'ticket_creation'
urlpatterns = [
    path('', views.create, name='create'),
    path('display/', views.list, name='display'),
    path('delete/', views.delete, name='delete'),
]