from django.db import models

# Create your models here.

class Test_1(models.Model):
  code = models.CharField(max_length=30)
  addr = models.CharField(max_length=20)

  def __str__(self):
    return self.addr