from django.urls import path
from fyr import views

app_name='fyr'
urlpatterns = [
    path('home/', views.index, name='index'),
    path('event_detail/<event_id>/', views.event_detail, name='event_detail'),
    # path('add_event/', views.add_event, name='add_event'),
    path('addresses/', views.address_list, name ='address_list'),
    path('address_list/add/', views.add_address, name ='add_address'),
]