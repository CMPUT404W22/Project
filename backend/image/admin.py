from django.contrib import admin

from image.models import Image

from django.utils.html import format_html


@admin.register(Image)
class Model1Admin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="200" height="200"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', ]

