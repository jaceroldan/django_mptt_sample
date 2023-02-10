from django.urls import path

from genres.views import show_genres

urlpatterns = [
    path('', show_genres),
]