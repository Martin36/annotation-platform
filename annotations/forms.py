from django import forms
from django.utils.translation import gettext_lazy as _

from annotations.enums import Category

LABEL_CHOICES = (
  (0, _("NOT Checkworthy")),
  (1, _("Checkworthy")),
  (2, _("Not applicable"))
)


class AnnotationForm(forms.Form):
  label = forms.ChoiceField(
    choices=LABEL_CHOICES,
    widget=forms.RadioSelect()
  )
  
  category = forms.ChoiceField(
    choices=Category.choices,
    widget=forms.Select(
      attrs= {
        "class": "form-control"
      }
    ))

  comment = forms.CharField(
    widget=forms.Textarea(
      attrs= {
        "class": "form-control",
        "placeholder": _("Write some words why you choose this label...")
      }
    ),
    required=False
  )