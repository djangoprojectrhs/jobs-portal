from django.contrib import admin
from JobsApp.models import hydjobs, bangalorejobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['company','title']

class bangalorejobsAdmin(admin.ModelAdmin):
    list_display=['company','title']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(bangalorejobs,bangalorejobsAdmin)
