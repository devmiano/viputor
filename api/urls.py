from api.views import *
from django.urls import path

urlpatterns = [
    path('user/<pk>/', get_user),
    path('creator/new/', new_creator),
    path('moderator/new/', new_moderator),
    path('profile/<pk>/', ProfileView.as_view()),
]
