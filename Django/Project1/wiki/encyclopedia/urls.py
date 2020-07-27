from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:title>/", views.article, name="article")
]
