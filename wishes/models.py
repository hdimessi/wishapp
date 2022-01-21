from django.db import models
from django.contrib.auth.models import User

class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    granted = models.DateField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
