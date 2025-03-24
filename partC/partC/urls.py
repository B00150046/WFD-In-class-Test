from django.urls import path

from . import views

app_name = 'partC'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
]
