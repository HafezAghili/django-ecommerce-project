from django.urls import path
from .views import SignUpView , LogoutView , ChangePassView
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', ChangePassView.as_view(), name='password_change'),
    ]