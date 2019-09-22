from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    webpage = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, unique=True)
    content = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="img/")

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, unique=True)
    duration = models.IntegerField()
    fee = models.IntegerField()
    description = models.TextField()
    certification = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/img/")

    def __str__(self):
        return str(self.name)
