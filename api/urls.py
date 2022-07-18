from api.views import *
from django.urls import path

urlpatterns = [
    path('user/<pk>/', get_user),
    path('user/create-patron/', create_patron),
    path('profile/<pk>/', ProfileView.as_view()),
]
