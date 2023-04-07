from django.db import models


class Place(models.Model):
    title = models.CharField(
        'Название места',
        max_length=200
        )
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')
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
        related_name='places',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        db_index=True
        )
    image = models.ImageField('Файл картинки')
    number = models.IntegerField(
        'Номер картинки',
        null=True
        )

