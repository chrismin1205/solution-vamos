from django.db import models

# Create your models here.
class Work(models.Model):
  work_name = models.CharField(max_length=200)
  summary = models.TextField()
  requirements = models.TextField()
  documents = models.TextField()
  client_request = models.TextField()
  procedure = models.TextField()
  term = models.TextField()
  fee = models.TextField()
  ect = models.TextField()
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.work_name