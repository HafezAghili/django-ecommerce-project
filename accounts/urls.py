from django.urls import path
from .views import SignUpView , LogoutView
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]