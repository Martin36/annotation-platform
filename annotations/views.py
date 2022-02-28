from django.shortcuts import render
from annotations.forms import AnnotationForm
from annotations.models import Annotation, Claim

# Create your views here.

def annotation_index(request):
  return render(request, 'annotation_index.html', {})

def claim_list(request):
  claims = Claim.objects.all()
  context = {
    'claims': claims
  }
  return render(request, 'claim_list.html', context)

def claim_annotation(request, pk):
  claim = Claim.objects.get(pk=pk)
  
  form = AnnotationForm()
  if request.method == 'POST':
    form = AnnotationForm(request.POST)
    if form.is_valid():
      annotation = Annotation(
        label=form.cleaned_data["label"],
        comment=form.cleaned_data["comment"],
        claim=claim,
        # TODO: Check that this is the logged in user
        user=request.user
      )
      annotation.save()
      
  context = {
    "claim": claim,
    "form": form
  }
  return render(request, 'claim_annotation.html', context)