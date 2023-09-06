from django.urls import path
from .views import NoteListAPIView, NoteDetailAPIView, subscribeToNotesAPIView, NoteCreateAPIView #,NoteSearchListAPIView
urlpatterns=[
    path('add', NoteCreateAPIView.as_view(), name="add"),
    path("notes/<str:slug>", NoteDetailAPIView.as_view(), name="note"),
    path('notes', NoteListAPIView.as_view(), name="notes"),
    path('subscribers', subscribeToNotesAPIView.as_view(), name="subscribe"),
    
    # path("notes/search.<str:query>", NoteSearchListAPIView.as_view(), name="search")
]