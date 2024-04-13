from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserView, LogoutView

urlpatterns = [
    path('register', UserRegistrationView.as_view()),
    path('login', UserLoginView.as_view()),
    path('get', UserView.as_view()),
    path('logout', LogoutView.as_view())
]
