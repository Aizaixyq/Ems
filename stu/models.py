from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Student(models.Model):
    name = models.CharField(_('姓名'), max_length=10)
    age = models.IntegerField(_('年龄'))
    gender = models.CharField(_('性别'), max_length=10)