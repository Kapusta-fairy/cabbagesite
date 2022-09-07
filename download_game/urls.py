from django.urls import path
from download_game.views import show_download_game


urlpatterns = [
    path('', show_download_game, name='download_game')
]
