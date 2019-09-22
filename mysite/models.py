from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=264, blank=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=False)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'Contact'
