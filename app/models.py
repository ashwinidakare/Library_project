from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    qty = models.IntegerField()
    price = models.IntegerField()
    author = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'book'

    


