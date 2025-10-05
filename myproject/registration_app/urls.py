from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name='register_user_root'),  # Handle root URL
    path('register/', views.register_user, name='register_user'),
]
