from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Claim(models.Model):
  speaker = models.CharField(max_length=100)
  sent_sv = models.TextField()
  sent_en = models.TextField()
  sent_idx = models.IntegerField()
  paragraph_text_sv = models.TextField(blank=True)
  paragraph_text_en = models.TextField(blank=True)
  paragraph_idx = models.IntegerField()
  
class Annotation(models.Model):
  annotator_id = models.CharField(max_length=50)
  label = models.PositiveIntegerField()
  comment = models.TextField(blank=True)    # TODO: Should this be required?
  created_on = models.DateTimeField(auto_now_add=True)
  last_modified_on = models.DateTimeField(auto_now=True)
  claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  
  