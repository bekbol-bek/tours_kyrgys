from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.utils.text import slugify
class Product(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    discription = models.TextField(max_length=1000)

    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("У пользователя должен быть email адрес")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email адрес", max_length=255, unique=True)
    # другие поля...

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class TourCategory(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField(blank=True)



        def __str__(self):
            return self.name

class Tour(models.Model):
        category = models.ForeignKey(TourCategory, on_delete=models.CASCADE)
        title = models.CharField(max_length=255)
        description = models.TextField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        photo = models.ImageField(upload_to='photos/', blank=True, null=True)

        # Другие поля, которые вам нужны

        def __str__(self):
            return self.title

class EcosystemCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)



    def __str__(self):
        return self.name

class Ecosystem(models.Model):
    category = models.ForeignKey(EcosystemCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)


    def __str__(self):
        return self.title
