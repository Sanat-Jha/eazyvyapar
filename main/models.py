from django.db import models

# Create your models here.
class register(models.Model):
    first_name = models.CharField(max_length=3000)
    second_name = models.CharField(max_length=3000)
    email = models.CharField(max_length=3000)
    phone = models.CharField(max_length=3000)
    def __str__(self):
        return self.first_name

class query(models.Model):
    first_name = models.CharField(max_length=3000)
    second_name = models.CharField(max_length=3000)
    email = models.CharField(max_length=3000)
    phone = models.CharField(max_length=3000)
    query = models.TextField()
    def __str__(self):
        return self.first_name + ",   " + self.query[:20] + "..."