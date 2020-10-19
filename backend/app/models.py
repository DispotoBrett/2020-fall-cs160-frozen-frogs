from django.db import models
from django.contrib.auth.models import  User, Group

class List_Book(models.Model):
    '''Represents a book'''
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    isbn = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    class_used = models.CharField(max_length=300)

    def __str__(self):
        return f'''
            title: {self.title},
            author: {self.author},
            isbn: {self.isbn},
            subject: {self.subject},
            class: {self.class_used}
        '''

class Posting(models.Model):
    '''Represents a book posting on the site'''
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    description = models.CharField(max_length=10000)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Seller', related_name='Seller')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Buyer', related_name='Buyer')
    book = models.ForeignKey(List_Book, on_delete=models.CASCADE, verbose_name='Book', related_name='Book')

    def __str__(self):
        return f'''
                book:{self.book},
                title{self.title},
                price: {self.price},
                description: {self.description}
                ''' 

class Favorite(models.Model):
    '''Allows user to save a book for later'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='User')
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, verbose_name='FavoritedPost', related_name='FavoritedPost')

class Message(models.Model):
    '''Represents a message between users'''
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ToUser', related_name='ToUser+')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='FromUser', related_name='FromUser+')
    message_text = models.CharField(max_length=300)
 
    def __str__(self):
        return f'{from_user} said to {to_user}: {message_text}' 

class Register(models.Model):
    ''' 
    We might not actually want this.
    Not to be saved to the database, but usefulf for creating forms
    '''
    sjsu_id = models.CharField(max_length = 9) # ID max length
    sjsu_pw = models.CharField(max_length = 50)
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.sjsu_id},{self.sjsu_pw},{self.name}'

