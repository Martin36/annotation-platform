from django import forms
from django.utils.translation import gettext as _

LABEL_CHOICES = (
  (0, _("NOT Checkworthy")),
  (1, _("Checkworthy"))
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
        "placeholder": _("Write some words why you choose this label...")
      }
    ),
    required=False
  )