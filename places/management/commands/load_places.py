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
            images_quantity_to_load = len(place_description['imgs'])
            number_of_images = place.images.all().count()
            if images_quantity_to_load!=number_of_images:
                for img_id, image_url in enumerate(place_description['imgs'], start=1):
                    image = requests.get(image_url)
                    image.raise_for_status()
                    image_name = f'{place_description["title"]}_{img_id}.jpg'
                    Image.objects.get_or_create(
                    image=ContentFile(
                        image.content,
                        name=image_name
                        ),
                        place=place,
                        number=img_id,
                        )
                logger.info(' Место успешно внесено в базу данных')
            else:
                raise MultipleObjectsReturned
        except requests.HTTPError:
            logger.warning('Проблемы при загрузке json файла')
