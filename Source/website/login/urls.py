from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log_out/', views.log_out, name='logout')
]
