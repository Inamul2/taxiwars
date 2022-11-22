from django.urls import path
from .views import *
urlpatterns = [
    path('create/', createBoard.as_view()),
    path('getBoard/', getBoard.as_view()),
    path('updateBoard/', updateBoard.as_view()),
    path('listBoards/', listBoard.as_view()),
]
