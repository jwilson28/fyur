from django.urls import path
from fyr import views

app_name='fyr'
urlpatterns = [
    path('', views.index, name='index'),
    path('event_detail/<event_id>/', views.event_detail, name='event_detail'),
    path('event/add', views.add_event, name='add_event'),
    path('addresses/', views.address_list, name ='address_list'),
    path('address_list/add/', views.add_address, name ='add_address'),
    path('bands/', views.band_list, name='band_list'),
    path('bands/add/', views.add_band, name='add_band'),
    path('venues/', views.venue_list, name='venue_list'),
    path('venues/add', views.add_venue, name='add_venue'),
]