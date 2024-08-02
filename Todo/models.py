from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})