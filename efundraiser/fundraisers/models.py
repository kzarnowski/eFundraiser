from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fundraiser(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    amount_to_raise = models.FloatField()
    amount_raised = models.FloatField()
    # user can't delete account when having open fundraisers
    # user = models.ForeignKey(User, on_delete=models.PROTECT)