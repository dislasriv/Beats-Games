from django.urls import path
from . import views


app_name = "posts"

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('user-playlists', views.user_posts_list, name="user-playlists"),
    path('new-post', views.new_post, name="new-post"),
    path('<slug:slug>', views.post_page, name="page"),
    path('<str:playlistId>/edit', views.edit_post, name="edit-post"),
]