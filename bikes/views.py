from django.shortcuts import render

from .forms import BikeForm
# Create your views here.

def index(request, template_name='index.html'):
    form = BikeForm(request.POST or None)
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
    form = BikeForm(request.POST or None)
    return render(request, template_name, {'form': form})
