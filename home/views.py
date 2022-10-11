from django.shortcuts import render, redirect
from django.views import View
from .models import *


# Create your views here.

def index(request):
    if request.method == "GET":
        # wall = wallpaper.objects.all()
        context = {"Tittle": "index"}
        return render(request, "index.html", context)


def all(request):
    if request.method == "GET":
        movies = Movies.objects.all()
        context = {"Tittle": "all","data": movies}
        return render(request, "all.html", context)

def download_board(request, pk):
    if request.method == "GET":
        # wall = wallpaper.objects.all()
        move = Movies.objects.get(id=pk)
        context = {"Tittle": "download_board","data":move}
        return render(request, "download_board.html", context)


def final(request, pk):
    if request.method == "GET":
        # wall = wallpaper.objects.all()
        move = Movies.objects.get(id=pk)
        context = {"Tittle": "final","data":move}
        return render(request, "final.html", context)