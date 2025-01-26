# account/urls.py

# 📦 Import necessary modules and classes
from django.urls import path
from . import views

# 📜 Define URL patterns for the account app
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('o/logout/', views.auth_logout_view, name='auth_logout'),
]