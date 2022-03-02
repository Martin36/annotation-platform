from django import forms

LABEL_CHOICES = (
  (0, "NOT Checkworthy"),
  (1, "Checkworthy")
)

class AnnotationForm(forms.Form):
  label = forms.ChoiceField(
    choices=LABEL_CHOICES,
    widget=forms.RadioSelect
  )

  comment = forms.CharField(
    widget=forms.Textarea(
      attrs={
        "class": "form-control",
        "placeholder": "Write some words why you choose this label..."
      }
    ),
    required=False
  )