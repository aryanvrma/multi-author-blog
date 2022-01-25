from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class post(models.Model):
    title = models.CharField(max_length = 101)
    content = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    image = models.ImageField(default = None,upload_to='post_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

  