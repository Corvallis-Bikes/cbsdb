from django.forms import ModelForm

from bikes.models import Bike

class BikeForm(ModelForm):
    class Meta:
        model = Bike
        fields = ['model','biketype_id','vin','state_id',
                  'description']
