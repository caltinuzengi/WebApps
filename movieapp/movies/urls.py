from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/series
# http://127.0.0.1:8000/movies/<int:id>
# http://127.0.0.1:8000/series/<int:id>

urlpatterns = [
    path("", views.home, name="homePage"),
    path("home", views.home, name="homePage"),
    path("movies", views.movies, name="moviePage"),
    path("series", views.series, name="seriesPage"),
    path("movies/<int:id>", views.details, name="details")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 