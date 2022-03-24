from django.urls import path
from . import views

urlpatterns = [
  path("", views.annotation_index, name="annotation_index"),
  path("annotation-list", views.annotation_list, name="annotation_list"),
  path("annotation/<int:pk>/", views.claim_annotation, name="claim_annotation"),
  path("annotate-next-claim", views.annotate_next_claim, name="annotate_next_claim"),
]