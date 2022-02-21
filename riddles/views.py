from re import template
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage

from main.models import Art
from .forms import ArtForm
from django.views.generic import FormView

 
class News(FormView):
    model = Art 
    template_name = 'riddles/datails_viws.html'
    context_objecct_name = 'art'




    
def index(request):
    error = ''
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
            return redirect('home')
    form = ArtForm() 
    data = {
        "form": form,
        "error": error
    }
    return render(request, 'riddles/index.html', data)




