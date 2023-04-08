from where_to_go import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.show_map)
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )