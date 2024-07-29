from django.db import models 

class CustomManager(models.Manager):
    def get_queryset(self):   # overriding Built-in method called when we call all()
        return super().get_queryset().order_by('name')  # now the base queryset is overrided with base + ordered by name = all.order_by('name')