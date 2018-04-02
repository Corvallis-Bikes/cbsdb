from django.forms import ModelForm

from app.models import Bike

class BikeForm(ModelForm):
    class Meta:
        model = Bike
