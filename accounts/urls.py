from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.views import home_view, signup_view, activate, activation_sent_view

account_patterns = [

    path('', home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('sent/', activation_sent_view, name='activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),

    # Password reset urls
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='accounts/password_change_done.html', name='password_change_complete')),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name='accounts/password_change.html', name='password_change')),
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_done.html', name='password_reset_done')),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html', name='password_reset_confirm')),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html', name='password_reset')),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html', name='password_reset_complete')),



]