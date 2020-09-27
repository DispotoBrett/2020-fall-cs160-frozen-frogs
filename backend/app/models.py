from django.db import models
from django.contrib.auth.models import  User, Group

class Posting(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    description = models.CharField(max_length=10000)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Seller', related_name='Seller')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Buyer', related_name='Buyer')

    def __str__(self):
        return f'{self.title} Posted by {self.seller}'
