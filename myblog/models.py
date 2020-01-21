from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("myblog:detail", kwargs={'pk':self.pk})
