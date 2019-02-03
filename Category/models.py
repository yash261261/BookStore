from django.db import models


# Create your models here.
class Author(models.Model):

    author_fname = models.CharField(max_length=50)
    author_lname = models.CharField(max_length=50)
    rating_user = models.FloatField()

    def __str__(self):
        return self.author_fname + " " + self.author_lname

class Books(models.Model):

    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    years = models.DateField()
    rating_user = models.FloatField()
    author = models.ForeignKey(Author, models.SET_NULL, null=True)

    def __str__(self):
        return self.title




