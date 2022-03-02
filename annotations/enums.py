from enum import Enum


class AnnotationCategory(Enum):
  OPINION = "OPINION"
  FUTURE_PREDICTION = "FUTURE_PREDICTION"
  IMPOSSIBLE = "IMPOSSIBLE"
  UNINTERESTING = "UNINTERESTING"
  NEEDS_CONTEXT = "NEEDS_CONTEXT"
  
  @classmethod
  def choices(cls):
    return tuple((i.name, i.value) for i in cls)