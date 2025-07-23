from django.urls import path

from accounts import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('login/' , views.login_page, name='login_page'),
    path('register/' , views.register, name='register'),
    path('verify-account/<token>/', views.verify_email_token, name='verify_email_token'),
]
