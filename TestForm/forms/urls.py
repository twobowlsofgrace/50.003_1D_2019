from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('basicform/', views.basic_form, name='basicform'),
]

