from django.db import models
from django.utils import timezone
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Bike(models.Model):
    BIKE_CHOICES = (
                    ('RD', 'Road'),
                    ('MT', 'Mountain'),
                    ('H', 'Hybrid'),
                    ('CB', 'Cruiser'),
                    ('RT', 'Recumbent'),
                    ('TM', 'Tandem'),
                    ('F', 'Folding'),
                    ('TR', 'Trike'),
                    ('UN', 'Unicycle'),
                    ('K', 'Kids'),

    STATE_CHOICES = (
                     ('G', 'Green Tag'),
                     ('B', 'Blue Tag'),
                     ('Y', 'Yellow Tag'),
                     ('W', 'White Tag'),
                     ('O', 'Orange Tag'))
                     ('R', 'Red Tag'))

    COLOR_CHOICES = (
                     ('V', 'Violet'),
                     ('IN', 'Indego'),
                     ('BL', 'Blue'),
                     ('TR', 'Turquoise'),
                     ('GR', 'Green'),
                     ('Y', 'Yellow'),
                     ('GD', 'Gold'),
                     ('O', 'Orange'),
                     ('R', 'Red'),
                     ('M', 'Magenta'),
                     ('BR', 'Brown'),
                     ('BL', 'Black'),
                     ('W', 'White'))


    # id (pk) key is atomatically created by django
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
        """
        String for representing the Model object.
        """
        return self.model
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('bike-detail', args=[str(self.id)])
