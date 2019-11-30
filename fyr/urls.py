from django.urls import path
from fyr import views

app_name='fyr'
urlpatterns = [
    path('home/', views.index, name='index'),
    path('event_detail/<event_id>/', views.event_detail, name='event_detail'),
    path('add_event/', views.add_event, name='add_event'),
]