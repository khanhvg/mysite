from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="media/product/")

    def __str__(self):
        return str(self.name)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to="media/user/", blank=True)

    def __str__(self):
        return self.user.username
