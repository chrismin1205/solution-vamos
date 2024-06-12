from django.db import models

# Create your models here.
class Work(models.Model):
  work_name = models.CharField(max_length=200, null=True)
  summary = models.TextField(null=True)
  requirements = models.TextField(null=True)
  documents = models.TextField(null=True)
  client_request = models.TextField(null=True)
  procedure = models.TextField(null=True)
  term = models.TextField(null=True)
  fee = models.TextField(null=True)
  ect = models.TextField(null=True)
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.work_name