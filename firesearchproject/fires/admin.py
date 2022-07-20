from django.contrib import admin
from .models import Fire
# Register your models here.

class FireAdmin(admin.ModelAdmin):
    list_display = ("_id","title","date","type_id","lon","lat")

admin.site.register(Fire, FireAdmin)