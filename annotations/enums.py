from enum import Enum
from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.TextChoices):
  NONE = "", _("None")
  OPINION = "Opinion", _("Opinion")
  PREDICTION = "Prediction", _("Prediction")
  TOO_GENERAL = "Too general", _("Too general")
  IMPOSSIBLE = "Impossible", _("Impossible")
  UNINTERESTING = "Uninteresting", _("Uninteresting")
  NEEDS_CONTEXT = "Needs context", _("Needs context")
