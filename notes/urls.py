from django.urls import path
from .views import NoteListAPIView, NoteDetailAPIView, subscribeToNotesAPIView
urlpatterns=[
    path("notes/<str:slug>", NoteDetailAPIView.as_view(), name="note"),
    path('notes', NoteListAPIView.as_view(), name="notes"),
    path('subscribers', subscribeToNotesAPIView.as_view(), name="subscribe"),
]