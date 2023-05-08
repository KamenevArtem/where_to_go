import logging
import os

import requests

from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandParser
from places.models import Place, Image


logging.basicConfig()
logger = logging.getLogger('place_logger')
logger.setLevel(logging.INFO)


class Command(BaseCommand):
    help = 'Загрузка информации о месте'
    
    
    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            'place',
            type=str
        )
    
    def handle(self, *args, **options):
        try:
            response = requests.get(options['place'])
            response.raise_for_status()
            place_description = response.json()
            place, _ = Place.objects.update_or_create(
                title=place_description['title'],
                defaults={
                    'description_short': place_description['description_short'],
                    'description_long': place_description['description_long'],
                    'lng': place_description['coordinates']['lng'],
                    'lat': place_description['coordinates']['lat'],
                }
            )
            for img_id, image_url in enumerate(place_description['imgs'], start=1):
                image = requests.get(image_url)
                image.raise_for_status()
                if Image.objects.filter(number=img_id).exists():
                    raise MultipleObjectsReturned
                Image.objects.get_or_create(
                image=ContentFile(
                    image.content,
                    name=f'{place_description["title"]}_{img_id}.jpg'
                    ),
                    place=place,
                    number=img_id,
                    )
            logger.info(' Место успешно внесено в базу данных')
        except requests.HTTPError:
            logger.warning('Проблемы при загрузке json файла')
