from django.forms import ModelForm
from django import forms
from bikes.models import Bike

class BikeForm(ModelForm):
    class Meta:
        model = Bike
        fields = ['model','bike_type','vin','state',
                  'description','created_at']

class BikeChoice(forms.Form):
    bikes = forms.ModelChoiceField(queryset=Bike.objects.all(),
                widget=forms.Select(attrs={"onChange":'this.form.submit();'}))
