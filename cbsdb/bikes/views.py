"""This module manages the rendering of html
and modifications to the database"""
# Stdlib imports
import copy

# Django Core imports
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.template.loader import render_to_string
from django.template import Template, Context
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from django.utils import timezone

# Third-Party imports
#from django_tables2 import RequestConfig, MultiTableMixin
#import numpy as np
from datetime import datetime

# Local app imports
from . import models, forms  # , fields as Fields


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_bikes=models.Bike.objects.all().count()
    # Available books (status = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_bikes':num_bikes},
    )

def addbike(request, template_name='add.html'):
    form = forms.BikeForm(request.POST or None)
    if request.method == 'POST':
        form = forms.BikeForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
        return redirect('bikelist')
    form = forms.BikeForm(request.POST or None)
    return render(request, template_name, {'form': form})

def waiver(request, template_name='waiver.html'):
    form = forms.UserForm()
    p_form = forms.PeopleForm()
    context = {'form': form,
                'p_form': p_form}
    return render(request, template_name, context)

class BikeListView(generic.ListView):
    """
    creates bike_list variable that can be used in html
    """
    model = models.Bike
    paginate_by = 10

class BikeDetailView(generic.DetailView):
    """
    creates bike_list variable that can be used in html
    """
    model = models.Bike
