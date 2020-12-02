from django.contrib import admin
from . import models
# Register your models here.

class registerAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.register, registerAdmin)
class queryAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.query, queryAdmin)