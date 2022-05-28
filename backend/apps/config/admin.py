from django.contrib import admin

from . import models


class ImageAdmin(admin.ModelAdmin):
    ...


admin.site.register(models.Image)
admin.site.register(models.Invite)
