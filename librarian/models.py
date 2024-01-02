from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    shelf_no = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True, blank=True, editable=False)
    cover_image = models.URLField()

    def save(self, *args, **kwargs):
        if not self.isbn:
            self.isbn = str(uuid.uuid4().int)[:13]

        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
