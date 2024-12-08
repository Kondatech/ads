from django import forms
from .models import Realisation

class RealisationForm(forms.ModelForm):
    class Meta:
        model = Realisation
        fields = ['title', 'description', 'image', 'category']


#impression 

from django import forms
from .models import PrintFile

class PrintFileForm(forms.ModelForm):
    class Meta:
        model = PrintFile
        fields = ['file', 'name',  'contact', 'dimensions', 'paper_type', 'print_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            #'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du client'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre contact'}),
            'dimensions': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: A4'}),
            'paper_type': forms.TextInput(attrs={'class': 'form-control'}),
            'print_type': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex: 30 examplaire' }),
        }

# demande de devis 

from django import forms

class DevisForm(forms.Form):
    name = forms.CharField(
        label="Nom complet",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom complet'}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre email'}),
    )
    phone = forms.CharField(
        label="Numéro de téléphone",
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro de téléphone'}),
    )
    description = forms.CharField(
        label="Description de vos besoins",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Décrivez vos besoins'}),
    )

