from django.urls import path
from .views import (
    index, PostsView,
    return_to_home, create_post,
    user_information, search_posts,
    update_posts, delete_posts,
)

urlpatterns = [
    path("", search_posts, name="videos"),
    path("check/", index, name='check'),
    path("", return_to_home, name='homepage'),
    path("users/<int:pk>", user_information, name="user_information"),
    path("posts/", PostsView.as_view(), name='posts'),
    path("posts/update/<int:pk>", update_posts, name='update'),
    path("posts/delete/<int:pk>", delete_posts, name='delete'),
    path("posts/new_post", create_post, name='new_post')
]
