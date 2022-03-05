from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from annotations.forms import AnnotationForm
from annotations.models import Annotation, Claim

def annotation_index(request):
  return render(request, 'annotation_index.html', {})

def claim_list(request):
  claims = Claim.objects.all()
  context = {
    'claims': claims
  }
  return render(request, 'claim_list.html', context)

@login_required
def annotate_next_claim(request):
  last_annotation = Annotation.objects.filter(
      user__username=request.user
    ).order_by("-id").first()
  if last_annotation:
    next_annotation_id = last_annotation.id + 1
  else:
    next_annotation_id = 0
  return redirect(f"annotation/{next_annotation_id}")

@login_required
def claim_annotation(request, pk):
  claim = Claim.objects.get(pk=pk)
  user_annotation = claim.annotation_set.filter(user__username=request.user).first()
  
  form = get_form(user_annotation)
    
  if request.method == 'POST':
    form = AnnotationForm(request.POST)
    if form.is_valid():
      store_annotation(request, form, claim)
      # Redirect user to next claim to annotate
      return redirect(f"/annotation/{pk+1}")

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
  