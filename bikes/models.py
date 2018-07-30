from django.db import models
from django.utils import timezone
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField


class People(models.Model):
    ROLE_CHOICES = (
        (4, 'Admin'),
        (3, 'Manager'),
        (2, 'Volunteer'),
        (1, 'User'),
        (0, 'No Waiver'))
    FOUND_CHOICES = (
        (0, 'Internet'),
        (1, 'FaceBook'),
        (2, 'Friend'),
        (3, 'Event'),
        (4, 'Flyer'),
        (5, 'Random'),
        (6, 'Other'))
    WHY_CHOICES = (
        (0, 'Work on own bike'),
        (1, 'Work on friends bike'),
        (2, 'Buy bike'),
        (3, 'Get parts'),
        (4, 'Volunteer'),
        (5, 'Other'))
    GENDER_CHOICES = (
        (1, 'Female'),
        (2, 'Male'),
        (3, 'TransMale'),
        (4, 'TransFemale'),
        (5, 'Gender NonConforming'),
        (6, 'Something Else'),
        (7, 'Decline to Answer'))
    PRONOUN_CHOICES = (
        (1, 'He'),
        (2, 'She'),
        (3, 'They'),
        (4, 'Ze'),
        (5, 'N/A'),
        (6, 'No Preference'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True, primary_key=True)
    first = models.CharField(max_length=30, blank=True)
    last = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, default='')

    address_1 = models.CharField(_("address"), max_length=128)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Corvallis")
    state = USStateField(_("state"), default="OR")
    zip_code = USZipCodeField(_("zip code"), default="97330")

    whyhere_id = models.IntegerField(choices=WHY_CHOICES,
                                      default=None, null=True)
    foundhow_id = models.IntegerField(choices=FOUND_CHOICES,
                                       default=None, null=True)
    volunteer_hrs = models.IntegerField(default=0)
    bench_hrs = models.IntegerField(default=0)
    birth_date = models.DateField(null=True, blank=True)
    gender_id = models.IntegerField(choices=GENDER_CHOICES,
                                      default=None, null=True)
    pronoun_id = models.IntegerField(choices=PRONOUN_CHOICES,
                                      default=None, null=True)
    role_id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,
                                               null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        people.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.people.save()

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
                    ('K', 'Kids'))

    STATE_CHOICES = (
                     ('G', 'Green Tag'),
                     ('B', 'Blue Tag'),
                     ('Y', 'Yellow Tag'),
                     ('W', 'White Tag'),
                     ('O', 'Orange Tag'),
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
    donor_people_id = models.ForeignKey(to=People,
                                        null=True, blank=True,
                                        related_name='donor_bike_set',
                                        on_delete=models.deletion.SET_NULL)
    donation_date = models.DateField(auto_now_add=True)
    disposal_date = models.DateField(blank=True)
    state_id = models.CharField(max_length=2,
                                choices=STATE_CHOICES,
                                default='WT')
    value = models.DecimalField(max_digits=6, decimal_places=2)
    manager_people_id = models.ForeignKey(to=People,
                                          null=True,
                                          related_name='manager_bike_set',
                                          on_delete=models.deletion.SET_NULL)
    owner_people_id = models.ForeignKey(to=People,
                                        null=True, blank=True,
                                        related_name='owner_bike_set',
                                        on_delete=models.deletion.SET_NULL)

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
                     ('PP', 'PayPal'))

    sale_time = models.DateTimeField(auto_now=True, primary_key=True)
    manager_people_id = models.ForeignKey(to=People,
                                          null=True,
                                          related_name='manager_sale_set',
                                          on_delete=models.deletion.SET_NULL)
    buyer_people_id = models.ForeignKey(to=People,
                                        null=True, blank=True,
                                        related_name='buyer_sale_set',
                                        on_delete=models.deletion.SET_NULL)
    salestype_id = models.IntegerField(choices=SALES_CHOICES,
                                       default='CM')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField(null=True)
    bike_id = models.ForeignKey(to=Bike,
                                null=True, blank=True,
                                on_delete=models.deletion.SET_NULL)
    notes = models.TextField(null=True)

class UseLog(models.Model):
    in_time = models.DateTimeField(auto_now=True, primary_key=True)
    out_time = models.DateTimeField()
    user_people_id = models.ForeignKey(to=People,
                                         null=True, blank=True,
                                         on_delete=models.deletion.SET_NULL)
    volunteering = models.BooleanField(default=False)
    bench = models.IntegerField(null=True, blank=True)

class ShiftLog(models.Model):
    in_time = models.DateTimeField(auto_now_add=True, primary_key=True)
    out_time = models.DateTimeField()
    open_manager_people_id = models.ForeignKey(to=People,
                                               related_name='openman_shiftlog_set',
                                               on_delete=models.deletion.SET_NULL)
    open_manager_people_id = models.ForeignKey(to=People,
                                               null=True, blank=True,
                                               related_name='closeman_shiftlog_set',
                                               on_delete=models.deletion.SET_NULL)
    in_cash = models.DecimalField(max_digits=6, decimal_places=2)
    out_cash = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    in_memo = models.TextField(null=True, blank=True)
    out_memo = models.TextField(null=True, blank=True)
