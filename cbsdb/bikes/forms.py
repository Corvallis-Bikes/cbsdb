from django.forms import ModelForm
from django.contrib.auth import get_user_model
User = get_user_model()

from bikes import models

class BikeForm(ModelForm):
    class Meta:
        model = models.Bike
        fields = ['make', 'model','biketype_id','vin','state_id',
                  'description', 'value']

class BikeChoice(forms.Form):
    bikes = forms.ModelChoiceField(queryset=models.Bike.objects.all(),
                widget=forms.Select(attrs={"onChange":'this.form.submit();'}))

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PeopleForm(ModelForm):
    class Meta:
        model = models.People
        fields = ('address_1', 'address_2', 'city', 'state', 'zip_code',
                    'whyhere_id', 'foundhow_id', 'birth_date', 'gender_id',
                    'pronoun_id')

