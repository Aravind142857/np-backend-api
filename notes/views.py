from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Note, User
from .serializers import NoteSerializer,UserSerializer

# Create your views here.

class NoteListAPIView(generics.ListAPIView):
    serializer_class= NoteSerializer
    def get_queryset(self):
        return Note.objects.all()
# class NoteSearchListAPIView(generics.ListAPIView):
#     serializer_class = NoteSerializer
#     def get(seld, request, query):
#         query_set = Note.objects.filter(title__contains=query)
#         if query_set:
#             return response.Response(seld.serializer_class(query_set).data)
#         return response.Reponse('Not found', status=status.HTTP_404_NOT_FOUND )
    
class NoteDetailAPIView(generics.ListAPIView):
    serializer_class= NoteSerializer
    def get(self, request, slug):
        print("request")
        query_set= Note.objects.filter(slug=slug).first()
    
        if query_set:
            return response.Response(self.serializer_class(query_set).data)
        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND )
    
class subscribeToNotesAPIView(generics.CreateAPIView):
    serializer_class= UserSerializer

    
    def get_queryset(self):
        return User.objects.all()
