from django.db import models
from django.core.validators import MinLengthValidator


class Make(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Enter a make (e.g. McLaren)',
        validators=[MinLengthValidator(2, 'Make must be greater than 1 character.')]
    )

    def __str__(self):
        """"String for representing the Model object."""
        return self.name

class Auto(models.Model):
    nickname = models.CharField(
        max_length=200,
        help_text='Enter a nickname.',
        validators=[MinLengthValidator(2, 'Nickname must be greater than 1 character.')]
    )
    mileage = models.PositiveBigIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    def __str__(self):
        """"String for representing in the admin list"""
        return self.nickname
