from django.contrib import admin
from .models import DogsModel, SomeKeys

admin.site.register(DogsModel)
admin.site.register(SomeKeys)
