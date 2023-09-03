from django.contrib import admin
from .models import Note, User

class NoteModelAdmin(admin.ModelAdmin):
    list_display =('title', 'created_at', 'updated_at')
    search_fields=('title','description')
    list_per_page=10
class UserModelAdmin(admin.ModelAdmin):
    list_display =('email', 'note', 'created_at')
    search_fields=('email','note__title')
    list_per_page=10
admin.site.register(Note, NoteModelAdmin)
admin.site.register(User, UserModelAdmin)
# Register your models here.
