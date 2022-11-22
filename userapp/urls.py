from django.urls import path
from .views import *
urlpatterns = [
    path('create/', createUser.as_view()),
    path('update/', updateUser.as_view()),
    path('login/', loginUser.as_view()),
    path('logout/', logoutUser.as_view()),
    path('delete/', deleteUser.as_view()),
]
