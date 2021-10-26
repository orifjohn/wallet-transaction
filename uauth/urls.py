from django.urls import path
from .views import register_view, logout_view, login_view

urlpatterns = [
    path('register/', register_view, name='register_url'),
    path('logout/', logout_view, name='logout_url'),
    path('login/', login_view, name='login_url'),
]
