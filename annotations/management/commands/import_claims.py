import csv, requests
import codecs
from contextlib import closing
from datetime import date

from annotations.models import Claim
from django.core.management.base import BaseCommand

class Command(BaseCommand):
  help = "Imports claims data from csv file"
  
  def handle(self, *args, **options):
    dropbox_link = "https://www.dropbox.com/s/5x5y5aq6hs7ulmw/partiledardebatt-22-01-12-cleaned-filtered.csv?dl=1"
    with closing(requests.get(dropbox_link, stream=True)) as r:      
      reader = csv.reader(codecs.iterdecode(r.iter_lines(), "utf-8"))
      claims = []
      for idx, row in enumerate(reader):
        if idx == 0: continue
        claim = Claim(
          idx = int(row[1]),
          speaker = row[2],
          sent_sv = row[3],
          sent_en = row[4],
          sent_idx = int(row[5]),
          paragraph_text_sv = row[6],
          paragraph_text_en = row[7],
          paragraph_idx = int(row[8]),
          date = date.fromisoformat("2022-01-12")
        )
        claims.append(claim)
      Claim.objects.bulk_create(claims)

    self.stdout.write(
      self.style.SUCCESS(
        'Successfully stored claims from "%s"' % dropbox_link))

      
    