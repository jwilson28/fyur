from django.urls import path
from fyr import views

urlpatterns = [
    path('home/', views.index, name='index'),
]