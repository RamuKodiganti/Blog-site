
from django.urls import path
from .views import RegisterView
from django.contrib.auth import views as auth_views  # Built-in views related to authentication and user management

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='usersapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usersapp/logout.html'), name='logout')
]
