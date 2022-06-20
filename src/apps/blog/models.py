from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    published = models.BooleanField(default=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
