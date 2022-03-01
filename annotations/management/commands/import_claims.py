import csv
from annotations.models import Claim
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
  help = "Imports claims data from csv file"
  
  def add_arguments(self, parser):
    parser.add_argument("data_file", type=str)

  def handle(self, *args, **options):
    # data_file = "data/partiledardebatt-22-01-12-filtered.csv"
    data_file = options["data_file"]
    
    with open(data_file) as f:
      reader = csv.reader(f)
      claims = []
      for idx, row in enumerate(reader):
        if idx == 0: continue
        claim = Claim(
          idx = int(row[0]),
          speaker = row[2],
          sent_sv = row[3],
          sent_en = row[4],
          sent_idx = int(row[5]),
          paragraph_text_sv = row[6],
          paragraph_text_en = row[7],
          paragraph_idx = int(row[8])
        )
        claims.append(claim)
      Claim.objects.bulk_create(claims)

    self.stdout.write(
      self.style.SUCCESS(
        'Successfully stored claims from "%s"' % data_file))

      
    