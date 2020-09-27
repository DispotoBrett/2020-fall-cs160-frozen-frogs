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

# Class for login. Trigger Login -> Logout
class Login(models.Model):
	sjsu_id = models.CharField(max_length = 9) # ID max length
	sjsu_pw = models.CharField(max_length = 50)

	def __str__(self):
		return f'{self.sjsu_id},{self.sjsu_pw}'

# Class for login. Trigger Login -> Logout
class List_Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    isbn = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    class_used = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title}/{self.author}/{self.isbn}/{self.subject}/{self.class_used}'