from django.shortcuts import render

# Create your views here.

def index(request, template_name='index.html'):
    form = BikeForm(request.POST or None)
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES,
                            user    = request.user,
                            initial = initial_values)
        if form.is_valid():
            pass

    return render(request, template_name, {'form': form})
