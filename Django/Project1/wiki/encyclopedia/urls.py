from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random/", views.random_page, name="random"),
    path("new/", views.new, name="new"),
    path("<slug:title>/", views.article, name="article")
]
    
