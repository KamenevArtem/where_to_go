import pathlib

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Place


def place_response(request, id):
    place = get_object_or_404(Place, id=id)
    images = place.images.all()
    details = {
        "title": place.title,
        "imgs": [img.image.url for img in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": f"{place.lat}",
            "lng": f"{place.lng}"
        }
    }
    return JsonResponse(
      details,
      json_dumps_params={'ensure_ascii': False, 'indent': 4},
      )


def index(request):
    script_path = pathlib.Path.cwd()
    places_path = script_path.joinpath('static/places')
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": f"{place.id}",
                "detailsUrl": reverse(place_response, kwargs={'id': place.id})
            }
        }
        features.append(feature)
    locations = {
        "type": "FeatureCollection",
        "features": features
    }
    return render(request, "index.html", context={"places": locations})
