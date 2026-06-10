from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):

    class Meta:
        model = Filme
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'style': 'width:100%;padding:12px;background:#2d2d2d;color:white;border:none;border-radius:8px;'}),
            'ano': forms.TextInput(attrs={'style': 'width:100%;padding:12px;background:#2d2d2d;color:white;border:none;border-radius:8px;'}),
            'diretor': forms.TextInput(attrs={'style': 'width:100%;padding:12px;background:#2d2d2d;color:white;border:none;border-radius:8px;'}),
            'genero': forms.TextInput(attrs={'style': 'width:100%;padding:12px;background:#2d2d2d;color:white;border:none;border-radius:8px;'}),
            'nota': forms.NumberInput(attrs={'style': 'width:100%;padding:12px;background:#2d2d2d;color:white;border:none;border-radius:8px;'}),
            'poster': forms.URLInput(attrs={'style': 'width:100%;padding:12px;background:#2d2d2d;color:white;border:none;border-radius:8px;'}),
        }   