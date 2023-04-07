from django.db import models


class Place(models.Model):
    title = models.CharField('Название места', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')
    lng = models.FloatField('Долгота' ,null=True)
    lat = models.FloatField('Широта' ,null=True)
