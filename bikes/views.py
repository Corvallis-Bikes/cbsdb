from .models import Bike
from .forms import BikeForm, BikeChoice
from django.views import generic
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
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
        return redirect('bikelist')
    form = BikeForm(request.POST or None)
    return render(request, template_name, {'form': form})

class BikeListView(generic.ListView):
    """
    creates bike_list variable that can be used in html
    """
    model = Bike
    paginate_by = 10

class BikeDetailView(generic.DetailView):
    """
    creates bike_list variable that can be used in html
    """
    model = Bike

def BikeSelect(request):
    bike_list  = BikeChoice()
    if request.GET.get('bikes'):  # also works with push!!
        selected = request.GET.get('bikes')
        query_results = Bike.objects.filter(id=selected)
        #get_object_or_404(Bike, pk=request.POST.get('id'))
        # get the user you want (connect for example) in the var "user"
    else:
        query_results = Bike.objects.order_by('-id')[:5] #reverse then take first 5

    context = {
            'query_results': query_results,
            'bike_list': bike_list,
            }

    return render(request, 'bikes/bike_select.html', context)
