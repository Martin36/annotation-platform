from urllib import response
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
  
  def setUp(self):
    self.client = Client()
  
  
  def test_annotation_index_GET(self):
    response = self.client.get(reverse("annotation_index"))
    
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, "annotation_index.html")
    
  def test_claim_list_GET(self):
    pass
  
  def test_annotate_next_claim_GET(self):
    pass
  
  def test_claim_annotation_GET(self):
    pass
  
