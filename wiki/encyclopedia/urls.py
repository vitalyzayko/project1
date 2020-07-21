from django.urls import path
from . import views

app_name="wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/new_entry", views.new_entry, name="new_entry"),
    path("wiki/new_entry/save", views.save_new_entry, name="save_new_entry"),
    path("wiki/query", views.query, name="query"),
    path("wiki/random_page", views.random_page, name="random_page"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("wiki/<str:title>/save", views.save, name="save_entry"),
    path("wiki/<str:title>", views.entry, name="entry"),

]

