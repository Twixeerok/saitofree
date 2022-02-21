from django.forms import widgets
from django.forms.widgets import TextInput
from main.models import Art
from django.forms import ModelForm, DateTimeInput, Textarea, ImageField


class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ['title', 'intro', 'full_text', 'price', 'data', 'image']


        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'intro': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            
            
            
            
            
        }
