import json
import pathlib

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Place, Image


def show_place(request, id):
    place = get_object_or_404(Place, id=id)
    return HttpResponse(place.title)


def index(request):
    script_path = pathlib.Path.cwd()
    places_path = script_path.joinpath('static/places')
    places = Place.objects.all()
    features = []
    for place in places:
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
        with open (places_path.joinpath(f'{place.id}.json'), 'w', encoding='utf8') as json_file:
            json.dump(details, json_file, ensure_ascii=False, indent=4)
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": f"{place.id}",
                "detailsUrl": f'static/places/{place.id}.json'
            }
        }
        features.append(feature)
    locations = {
        "type": "FeatureCollection",
        "features": features
    }
    return render(request, "index.html", context={"places": locations})
