import json
import pathlib

from django.shortcuts import render
from .models import Place, Image


def index(request):
    script_path = pathlib.Path.cwd()
    places_path = script_path.joinpath('static/places')
    places = Place.objects.all()
    features = []
    for place in places:
        images = place.images.all()
        print(place.lat, place.lng)
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
