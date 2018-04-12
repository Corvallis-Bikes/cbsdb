from django.shortcuts import render
from django.views import generic
from .forms import BikeForm
from .models import Bike
# Create your views here.


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_bikes=Bike.objects.all().count()
    # Available books (status = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_bikes':num_bikes},
    )

def addbike(request, template_name='add.html'):
    form = BikeForm(request.POST or None)
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
    form = BikeForm(request.POST or None)
    return render(request, template_name, {'form': form})

class BikeListView(generic.ListView):
    """
    creates bike_list variable that can be used in html
    """
    model = Bike

class BikeDetailView(generic.DetailView):
    """
    creates bike_list variable that can be used in html
    """
    model = Bike
