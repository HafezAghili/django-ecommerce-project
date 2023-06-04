from django.urls import path
from .views import HomeView , ComingSoonView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('comingsoon/',ComingSoonView.as_view(),name='comingsoon'),
]