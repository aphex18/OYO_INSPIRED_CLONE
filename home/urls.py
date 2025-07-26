from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotel-description/<slug>/', views.hotel_description, name='hotel_description'),
]
