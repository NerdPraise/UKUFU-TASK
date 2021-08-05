from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.db.models.signals import post_save


GENDER_CHOICE = (
    ('Male', 'male'),
    ('Female', 'female'),
    ('Others', 'Others')
)


class Company(models.Model):
    name = models.CharField(max_length=50)
    index = models.IntegerField()


class Food(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Fruits(Food):
    user = models.ManyToManyField(
        'Person', related_name='fruits', symmetrical=False)


class Vegetable(Food):
    user = models.ManyToManyField(
        'Person', related_name='vegetables', symmetrical=False)


class Person(models.Model):
    username = models.CharField(max_length=120)
    guid = models.CharField(max_length=50, unique=True)
    has_died = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ImageField()
    age = models.IntegerField()
    eye_color = models.CharField(max_length=12, null=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=6)
    about = models.TextField()
    registered = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    phone = PhoneNumberField()
    greeting = models.TextField()
    friends = models.ManyToManyField('self', symmetrical=False)
    company = models.ForeignKey(
        'Company', related_name='employee', blank=True, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            if isinstance(self.balance, str) and "$" in self.balance:
                balance = self.balance.replace('$', '').replace(',', '')
                self.balance = float(balance)

        return super().save(*args, **kwargs)
