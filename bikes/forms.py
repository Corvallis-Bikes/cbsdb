from django.forms import ModelForm

from bikes.models import Bike

class BikeForm(ModelForm):
    class Meta:
        model = Bike
        fields = ['model','bike_type','vin','state',
                  'description','created_at']
