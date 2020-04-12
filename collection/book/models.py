from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework.authtoken.models import Token



class User(AbstractUser):
    age = models.IntegerField(null = True, blank = True)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user(sender, instance, created, **kwargs):
        if created:
            if not instance.is_superuser:
                instance.set_password(instance.password)
                instance.is_active = True
                instance.save()
            token, _ = Token.objects.get_or_create(user=instance)

class Book(models.Model):
    title = models.CharField(max_length = 80)
    amazon_url = models.URLField(max_length = 200) 
    author = models.CharField(max_length =120)
    genre = models.CharField(max_length = 60)

    def __str__(self):
        return "{}-{}".format(self.title, self.author)

class BookUser(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'book_users')
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = 'books')
    is_fav = models.BooleanField(default = False)

    def __str__(self):
        return "{}-{}".format(self.user, self.book)


