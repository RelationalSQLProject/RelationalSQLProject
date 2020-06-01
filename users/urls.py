from django.urls import path
from users.views import home_view, signup_view


users_patterns = [
    path('home/', home_view, name='home'),
    path('signup/', signup_view, name='signup'),

]