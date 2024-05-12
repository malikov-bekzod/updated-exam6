from django.contrib import admin
from .models import Albom,Artist,Song
# Register your models here.
admin.site.register([Albom,Artist,Song])