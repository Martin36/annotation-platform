from pydoc import resolve
from django.test import SimpleTestCase
from django.urls import reverse
from annotations.views import annotation_index, claim_annotation

class TestUrls(SimpleTestCase):
  
  def test_index_url_is_resolved(self):
    url = reverse("annotation_index")
    self.assertEquals(resolve(url).func, annotation_index)
  
  def test_claim_list_url_is_resolved(self):
    url = reverse("claim_list")
    # TODO: 
    # self.assertEquals(resolve(url).func, annotation_index)
    
  def test_annotation_url_is_resolved(self):
    url = reverse("claim_annotation", args=['some-slug'])
    self.assertEquals(resolve(url).func, claim_annotation)
    
  def test_annotate_next_claim_url_is_resolved(self):
    pass
  
  
  
