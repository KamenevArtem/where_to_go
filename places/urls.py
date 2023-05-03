from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, place_response

urlpatterns = [
    path('', index, name='index'),
    path('places/<int:id>', place_response),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)