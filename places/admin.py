from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class PreviewMixin:
    @staticmethod
    def show_preview(obj):
        return format_html(
            '<img style="max-height:{height}" src="{url}"/>',
            height='200px',
            url=obj.image.url
        )


class ImageInline(SortableTabularInline, PreviewMixin):
    model = Image
    fields = ['place', 'show_preview', 'image']
    readonly_fields = ['show_preview']
    extra = 5


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'description_short', 'lng', 'lat')
    list_editable = ['description_short', 'lng', 'lat']
    pass


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin, PreviewMixin):
    list_display = ('id', 'show_preview', 'place', 'number')
    readonly_fields = ['show_preview']
