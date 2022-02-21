from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import Art
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
def index(request):
    main = Art.objects.order_by('data') 
    return render(request, 'main/index.html', {'main': main})

class News(DetailView):
    model = Art 
    template_name = 'riddles/datails_viws.html'
    context_objecct_name = 'Art'


    