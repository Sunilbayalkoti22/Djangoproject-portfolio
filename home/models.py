from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.TextField(blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=300)
    post = models.CharField(max_length=300)
    image = models.TextField(blank=True)
    review = models.TextField()

    def __str__(self):
        return self.name

class Info(models.Model):
    city = models.TextField(max_length=300)
    street = models.TextField(max_length=300)
    time = models.TextField(max_length=300)
    phone = models.IntegerField()
    email = models.EmailField(max_length=300)

    def __str__(self):
        return self.city

class Qualification(models.Model):
    name = models.CharField(max_length=300)
    data = models.CharField(max_length=300)
    result = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Myplan(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=300)
    forwhat = models.CharField(max_length=300)
    transfer = models.CharField(max_length=300)
    style = models.CharField(max_length=300)
    service = models.CharField(max_length=300)
    price = models.CharField(max_length=300)

    def __int__(self):
        return self.rank

class Fact(models.Model):
    name = models.CharField(max_length=300)
    num = models.IntegerField()

    def __str__(self):
       return self.name

