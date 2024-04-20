from django.urls import path
from .views import AddPostView, GetAllPostsView, GetAllPostsByUserView, GetPostByIdView

urlpatterns = [
    path('add', AddPostView.as_view()),
    path('', GetAllPostsView.as_view()),
    path('my-posts', GetAllPostsByUserView.as_view()),
    path('<int:post_id>', GetPostByIdView.as_view())
]
