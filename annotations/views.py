from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from annotations.forms import AnnotationForm
from annotations.helpers import find_first_missing_int
from annotations.models import Annotation, Claim

def annotation_index(request):
  return render(request, 'annotation_index.html', {})

def annotation_list(request):
  annotations = Annotation.objects.filter(
    user__username=request.user
  ).order_by("-claim__id")
  
  language = request.LANGUAGE_CODE

  context = {
    'annotations': annotations,
    'language': language
  }
  
  return render(request, 'annotation_list.html', context)

@login_required
def annotate_next_claim(request):
  annotated_claim_indices = get_annotated_indices_for_user(request.user)
  next_idx = find_first_missing_int(annotated_claim_indices)
  return redirect(f"/annotation/{next_idx}")

@login_required
def claim_annotation(request, pk):
  claim = Claim.objects.get(pk=pk)
  user_annotation = claim.annotation_set.filter(user__username=request.user).first()
  
  form = get_form(user_annotation)
    
  if request.method == 'POST':
    form = AnnotationForm(request.POST)
    if form.is_valid():
      store_annotation(request, form, claim)
      return annotate_next_claim(request)

  language = request.LANGUAGE_CODE
      
  context = {
    "claim": claim,
    "form": form,
    "language": language
  }
  
  return render(request, 'claim_annotation.html', context)


def get_form(user_annotation: Annotation):
  if user_annotation:
    form = AnnotationForm(initial={
      "label": user_annotation.label, 
      "comment": user_annotation.comment})
  else:
    form = AnnotationForm()
  return form  

def store_annotation(request, form, claim):
  annotation = Annotation(
    label=form.cleaned_data["label"],
    comment=form.cleaned_data["comment"],
    category=form.cleaned_data["category"],
    claim=claim,
    user=request.user
  )
  annotation.save()
  
def get_annotated_indices_for_user(user):
  annotations_by_user = Annotation.objects.filter(
    user__username=user
  ).order_by("-claim__id")
  return [annotation.claim.id for annotation in annotations_by_user]
