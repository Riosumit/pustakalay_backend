from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    batch = models.CharField(max_length=10)
    reg_no = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(limit_value=10, message='Phone number must be at least 10 characters.'),
            MaxLengthValidator(limit_value=10, message='Phone number must be at most 10 characters.')
        ]
    )