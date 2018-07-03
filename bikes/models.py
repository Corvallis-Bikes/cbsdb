from django.db import models
from django.utils import timezone

class Bike(models.Model):
    BIKE_CHOICES = (
                    ('RD', 'Road Bike'),
                    ('CB', 'Cruiser Bike'),
                    ('MT', 'Mountain Bike'))

    STATE_CHOICES = (
                    ('GT', 'Green Tag'),
                    ('WT', 'White Tag'),
                    ('BT', 'Black Tag'))

    model = models.TextField()
    bike_type = models.CharField(max_length=2,
                                    choices=BIKE_CHOICES,
                                    default='CB')
    vin = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=2,
                                choices=STATE_CHOICES,
                                default='WT')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.model
