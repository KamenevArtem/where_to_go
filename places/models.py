from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'Название места',
        max_length=200
        )
    description_short = models.TextField('Краткое описание')
    description_long = HTMLField('Полное описание', blank=True)
    lng = models.FloatField(
        'Долгота',
        null=True
        )
    lat = models.FloatField(
        'Широта',
        null=True
        )
    
    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        )
    image = models.ImageField('Файл картинки')
    number = models.IntegerField(
        'Номер картинки',
        default=0
        )
    
    class Meta:
        ordering = ['number']
    
    def __str__(self):
        return self.place.title

