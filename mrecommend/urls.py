from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("imagecapture", views.imagecapture, name="imageprocess"),
    path("detectemotion", views.detectemotion, name="detectemotion"),
    path("music", views.music, name='music'),
    path("movies", views.movies, name='movies')
]
