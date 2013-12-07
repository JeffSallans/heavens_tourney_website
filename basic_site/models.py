from django.db import models
from django.utils import timezone

# Create your models here.
class Interest(models.Model):
	sequencenum = models.IntegerField(primary_key = True)
	email = models.CharField(max_length = 70)
	date_created = models.DateTimeField(default=timezone.now)