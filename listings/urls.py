from django.urls import path

from .views import store_view

listing_patterns = [
    path('store/', store_view, name='store_view')
]