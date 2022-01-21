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

ACTIVITY_TYPES = [
    ("added", "added"),
    ("updated", "updated"),
    ("granted", "granted"),
    ("liked", "liked"),
]

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE) 
    type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.user.username + ' ' + self.type + ' ' + self.wish.title
