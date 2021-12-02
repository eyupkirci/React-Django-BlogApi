from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()


class Post(models.Model):  # ok
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/%Y", default="default.png")
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ("active", "active"),
        ("deactive", "deactive"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title + " " + self.status
