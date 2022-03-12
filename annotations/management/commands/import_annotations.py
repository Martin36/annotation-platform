import csv, math
import pandas as pd

from annotations.models import Annotation, Claim
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
  help = "Imports annotations data from csv file"
  
  def add_arguments(self, parser):
    parser.add_argument("data_file", type=str, default="")

  def handle(self, *args, **options):
    data_file = options["data_file"]
    df = pd.read_csv(data_file)
    df = df.where(pd.notnull(df), None) # Convert nans to Nones
    annotations = []
    user = User.objects.get(username="martin")
    
    for _, row in df.iterrows():
      claim = Claim.objects.filter(idx=row["Index"]).first()
      if not claim:
        continue
      if math.isnan(row["label_m"]):
        continue
      
      assert claim.sent_sv == row["sent_sv"]
      
      annotation = Annotation(
        annotator_id = "123",
        label = row["label_m"],
        claim = claim,
        user = user
      )      
      if row["comment_m"]:
        annotation.comment = row["comment_m"]
      annotations.append(annotation)
      
    Annotation.objects.bulk_create(annotations)

    self.stdout.write(
      self.style.SUCCESS(
        'Successfully stored annotations from "%s"' % data_file))

      
    