from django.db import models
from result.models import Work

# Create your models here.
class WorkName(models.Model):
  work = models.ForeignKey(Work, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.work