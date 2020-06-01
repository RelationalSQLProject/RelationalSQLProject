from django.contrib.auth import views as auth_views
from django.urls import path

from users.views import home_view, signup_view, activate, activation_sent_view

user_patterns = [
    path('', home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('sent/', activation_sent_view, name='activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),

]