from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

GENDER = [
    (0, 'M'),
    (1, 'F'),
    (2, 'Other'),
]

class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.PositiveSmallIntegerField(choices=GENDER)
    photo = models.ImageField(upload_to='media/photo/%Y/%m/%d', default="notfound")
    resume = models.FileField(upload_to='media/resume/%Y/%m/%d', default="notfound")


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    attachment = models.FileField(upload_to='media/attachment/%Y/%m/%d', default="notfound")


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.PositiveSmallIntegerField(choices=GENDER)
    photo = models.ImageField(upload_to='media/photo/%Y/%m/%d', default="notfound")
    resume = models.FileField(upload_to='media/resume/%Y/%m/%d', default="notfound")

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )