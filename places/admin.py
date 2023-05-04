from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image

class Preview:
    @staticmethod
    def show_preview(obj):
        return format_html(
            '<img style="max-height:{height}" src="{url}"/>',
            height='200px',
            url=obj.image.url
        )


class ImageInline(admin.TabularInline, Preview):
    model = Image
    fields = ['number', 'place', 'show_preview', 'image']
    readonly_fields = ['show_preview']
    extra = 5


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [
        ImageInline
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin, Preview):
    list_display = ('place', 'number', 'show_preview')
    list_editable = ['number']
    readonly_fields = ['show_preview']
