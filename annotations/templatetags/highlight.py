from django import template
from django.utils.safestring import mark_safe
from re import IGNORECASE, compile, escape

register = template.Library()

@register.filter(name='highlight')
def highlight(text, highlighted_text):
  regex = compile(escape(highlighted_text), IGNORECASE)
  return mark_safe(
    regex.sub(
      lambda m: '<b class="text-primary">{}</b>'.format(m.group()),
      text
    )
  )