from django.urls import path
from .views import HomePageView, AddmusicView, EditMusicView, MusicDetailView, MusicDeleteView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add_music/', AddmusicView.as_view(), name='add_music'),
    path('edit/<int:pk>/', EditMusicView.as_view(), name='edit_music'),
    path('player/<int:pk>', MusicDetailView.as_view(), name='music_player'),
    path('delete/<int:pk>', MusicDeleteView.as_view(), name='delete_music'),
]