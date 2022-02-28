from django.contrib import admin
from annotations.models import Claim, Annotation

# Register your models here.

class ClaimAdmin(admin.ModelAdmin):
  pass

class AnnotationAdmin(admin.ModelAdmin):
  pass

admin.site.register(Claim, ClaimAdmin)
admin.site.register(Annotation, AnnotationAdmin)