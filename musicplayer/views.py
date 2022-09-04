from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MusicPlayerModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    model = MusicPlayerModel
    template_name = 'home.html'

class AddmusicView(CreateView):
    template_name = 'new_music.html'
    model = MusicPlayerModel
    fields = ('title', 'author', 'music', 'image')
    success_url = reverse_lazy('home')

class EditMusicView(UpdateView):
    template_name = 'edit_music.html'
    model = MusicPlayerModel
    fields = ('title', 'author', 'music', 'image')
    success_url = reverse_lazy('home')

class MusicDetailView(DetailView):
    model = MusicPlayerModel
    template_name = 'music_player.html'

class MusicDeleteView(DeleteView):
    model = MusicPlayerModel
    template_name = 'music_delete.html'
    success_url = reverse_lazy('home')