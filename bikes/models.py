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


    id = models.AutoField(primary_key=True)
    make = models.TextField()
    model = models.TextField()
    vin = models.IntegerField(null=True, blank=True)
    color_id = models.CharField(max_length=2,
                                choices=BIKE_CHOICES,
                                default=None,
                                null=True)
    biketype_id = models.CharField(max_length=2,
                                 choices=BIKE_CHOICES,
                                 default=None,
                                 null=True)
    size = models.CharField(max_length=6,
                            blank=True)
    speeds = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    #donor_people_id = models.ForeignKey(to=,
    #                                     on_delete=models.deletion.SET_NULL)
    donation_date = models.DateField(auto_now_add=True)
    disposal_date = models.DateField(blank=True)
    state_id = models.CharField(max_length=2,
                                choices=STATE_CHOICES,
                                default='WT')
    value = models.DecimalField(max_digits=6, decimal_places=2)
    #manager_people_id = models.ForeignKey(to=,
    #                                       null=True,
    #                                       on_delete=models.deletion.SET_NULL)
    #owner_people_id = models.ForeignKey(to=,
    #                                     null=True,
    #                                     on_delete=models.deletion.SET_NULL)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return "%s %s %s" % (self.color_id, self.make, self.model)
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('bike-detail', args=[str(self.id)])

class Sale(models.Model):
    SALES_CHOICES = (
                     ('CM', 'Cash Money'),
                     ('CC', 'Credit Card'),
                     ('PP', 'PayPal'),

    sale_time=models.DateTimeField(auto_now=True, primary_key=True)
    #manager_people_id = models.ForeignKey(to=,
    #                                       null=True,
    #                                       on_delete=models.deletion.SET_NULL)
    #buyer_people_id = models.ForeignKey(to=,
    #                                     null=True,
    #                                     on_delete=models.deletion.SET_NULL)
    salestype_id = models.IntegerField(choices=Sales_CHOICES,
                                       default='CM')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField(null=True)
    bike_id = models.ForeignKey(to=Bike,
                                null=True,
                                on_delete=models.deletion.SET_NULL)
    notes = models.TextField(null=True)



