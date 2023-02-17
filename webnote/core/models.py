import uuid

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.PROTECT)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.PROTECT)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    title = models.CharField(max_length=100, default="Без названия")
    image = models.ImageField(upload_to="images", blank=True, null=True)
    content = models.TextField(blank=True)
    is_favorite = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
