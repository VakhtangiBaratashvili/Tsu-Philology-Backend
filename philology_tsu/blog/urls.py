from django.urls import path
from .views import AddPostView, GetAllPostsView, GetAllPostsByUserView

urlpatterns = [
    path('add', AddPostView.as_view()),
    path('', GetAllPostsView.as_view()),
    path('my-posts', GetAllPostsByUserView.as_view())
]
