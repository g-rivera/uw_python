from django.db import models

# Create your models here.

class book(models.Model):
    book_id   = models.CharField(max_length=3, primary_key=True)
    title     = models.CharField(max_length=100)
    isbn      = models.CharField(max_length=25)
    author    = models.CharField(max_length=70)
    publisher = models.CharField(max_length=85)
    publish_date = models.DateTimeField('Publishing date:')

    def __unicode__(self):
        return self.title


