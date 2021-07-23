from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICE = (
    ('Male', 'male'),
    ('Female', 'female'),
    ('Others', 'Others')
)


class User(AbstractUser):
    friends = models.ManyToManyField('User', blank=True)
    company = models.ForeignKey(
        'Company', related_name='employee', on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    guid = models.CharField(max_length=50, unique=True)
    has_died = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ImageField()
    age = models.IntegerField()
    eye_color = models.CharField(max_length=12, null=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=6)
    about = models.TextField()
    registerd = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    phone = PhoneNumberField()
    greeting = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            if isinstance(self.balance, str) and "$" in self.balance:
                balance = self.balance.replace('$', '').replace(',', '')
                self.balance = float(balance)

        return super().save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=50)
    index = models.IntegerField()


class Food(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Fruits(Food):
    user = models.ForeignKey(
        'User', related_name='user_fruits', on_delete=models.CASCADE)


class Vegetable(Food):
    user = models.ForeignKey(
        'User', related_name='user_veg', on_delete=models.CASCADE)
