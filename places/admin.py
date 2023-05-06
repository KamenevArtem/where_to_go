from adminsortable2.admin import SortableAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['place', 'image', 'show_preview']
    readonly_fields = ['show_preview']
    extra = 5
    def show_preview(self, obj):
        return format_html(
            '<img style="max-height:{height}" src="{url}"/>',
            height='200px',
            url=obj.image.url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = ('title', 'description_short', 'description_long', 'lng', 'lat')
    list_display = ('title', 'description_short', 'lng', 'lat')
    list_editable = ['description_short', 'lng', 'lat']
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'show_preview', 'place', 'number')
    readonly_fields = ['show_preview']
    def show_preview(self, obj):
        return format_html(
            '<img style="max-height:{height}" src="{url}"/>',
            height='200px',
            url=obj.image.url
        )
