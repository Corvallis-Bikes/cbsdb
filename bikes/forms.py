from django.forms import ModelForm
from django.contrib.auth.models import User

from bikes.models import Bike, People

class BikeForm(ModelForm):
    class Meta:
        model = Bike
        fields = ['model','biketype_id','vin','state_id',
                  'description']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ('address_1', 'address_2', 'city', 'state', 'zip_code',
                    'whyhere_id', 'foundhow_id', 'birth_date', 'gender_id',
                    'pronoun_id')
      