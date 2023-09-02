from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=24)
    description=models.TextField()
    uid=models.IntegerField(null=True, blank=True)
    slug=models.SlugField(max_length=50, null=True, blank=True)
    # uid=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now = True)

    class Meta:
        ordering=('-created_at',)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        to_assign=slugify(self.title)

        if Note.objects.filter(slug=to_assign).exists():
            to_assign = to_assign + str(Note.objects.all().count())
        self.uid=Note.objects.all().count()
        self.slug = to_assign
        super().save(*args, **kwargs)

class User(models.Model):
    note = models.ForeignKey(to=Note, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=254)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now = True)


    class Meta:
        ordering=('-created_at',)
    
    def __str__(self):
        return self.email