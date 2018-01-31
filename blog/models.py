from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Bags(models.Model):
    bags_id = models.ForeignKey('auth.user')
    bags_name = models.CharField(max_length=200)
    bags_color = models.CharField(max_length=200)
    bags_size = models.CharField(max_length=200)
    bag_added = models.DateTimeField(default=timezone.now)
