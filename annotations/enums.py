from enum import Enum
from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.TextChoices):
  OPINION = "Opinion", _("Opinion")
  PREDICTION = "Prediction", _("Prediction")
  IMPOSSIBLE = "Impossible", _("Impossible")
  UNINTERESTING = "Uninteresting", _("Uninteresting")
  NEEDS_CONTEXT = "Needs context", _("Needs context")
