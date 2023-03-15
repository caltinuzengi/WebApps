from django.shortcuts import render
from .models import Category, Media

# Create your views here.
# Sadik Turan

category_list = ["Adventure", "Horror", "Romantic", "Dram"]
media_list = [
    {
    "id": 1,
    "name" : "The Lord of the Rings",
    "description": "Extraordinary movie!",
    "image": "https://m.media-amazon.com/images/M/MV5BZGMxZTdjZmYtMmE2Ni00ZTdkLWI5NTgtNjlmMjBiNzU2MmI5XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
    "type": "movie",
    "homepage": True
    },
            {
    "id": 2,
    "name":"Hobbit",
    "description":"Excellent Movie!",
    "image":"https://tr.web.img4.acsta.net/pictures/210/562/21056253_20131108151938568.jpg",
    "type": "movie",
    "homepage": True
              },
              {
    "id": 3,
    "name": "Harry Potter",
    "description": "Nice Movie",
    "image":"https://m.media-amazon.com/images/M/MV5BNmQ0ODBhMjUtNDRhOC00MGQzLTk5MTAtZDliODg5NmU5MjZhXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_FMjpg_UX1000_.jpg",
    "type": "movie",
    "homepage": True
              },
            {
    "id": 4,
    "name": "John Wick",
    "description": "Martial Arts MasterPiece",
    "image":"https://m.media-amazon.com/images/M/MV5BMTU2NjA1ODgzMF5BMl5BanBnXkFtZTgwMTM2MTI4MjE@._V1_.jpg",
    "type": "movie",
    "homepage": True
              },
              {   
    "id": 5,     
    "name" : "LUTHER",
    "description": "Extraordinary serie!",
    "image": "https://m.media-amazon.com/images/M/MV5BZWM3MGE0YjEtNzdlMC00NmM3LWE1MmItN2E4ZDM4ZTllY2QzXkEyXkFqcGdeQXVyNzMwOTY2NTI@._V1_FMjpg_UX1000_.jpg",
    "type": "serie",
    "homepage": True
    },
            {
    "id": 6,
    "name":"SHERLOCK HOLMES",
    "description":"Excellent Movie!",
    "image":"https://m.media-amazon.com/images/M/MV5BMWEzNTFlMTQtMzhjOS00MzQ1LWJjNjgtY2RhMjFhYjQwYjIzXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_FMjpg_UX1000_.jpg",
    "type": "serie",
    "homepage": True
              },
              {
    "id": 7,
    "name": "BLACKLIST",
    "description": "Nice Main Character!",
    "image":"https://m.media-amazon.com/images/M/MV5BMTU1OTdjYTUtMzA2MS00Njg4LWI1NTctMWUzYzNkNmQ5YWY3XkEyXkFqcGdeQXVyMTUwMzM5ODkz._V1_FMjpg_UX1000_.jpg",
    "type": "serie",
    "homepage": True
              },
            {
    "id": 8,
    "name": "LUCIFER",
    "description": "Martial Arts MasterPiece",
    "image":"https://m.media-amazon.com/images/M/MV5BNDJjMzc4NGYtZmFmNS00YWY3LThjMzQtYzJlNGFkZGRiOWI1XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_FMjpg_UX1000_.jpg",
    "type": "serie",
    "homepage": True
              }        

    ]


def home(request):
    data = {
        #"categories": category_list,
        #"media": media_list
        "categories": Category.objects.all(),
        "media": Media.objects.filter(homepage = True)
    }
    return render(request, "index.html", data)


def movies(request):
    data = {
        "media": Media.objects.all()
    }
    return render(request, "movies.html", data)

def series(request):
    data = {
        "media": Media.objects.all()
    }
    return render(request, "series.html", data)

def details(request, id):
    data = {
        "media": Media.objects.get(id=id)
    }
    return render(request, "details.html", data)