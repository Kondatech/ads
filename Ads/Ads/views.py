from django.shortcuts import render
# les views des different pages
def home_view(request):
    return render(request, 'home.html')

from .models import Service

def service_view(resquest):
    services_list = Service.objects.all()
    return render(resquest, 'service.html', {'service': services_list})

def galerie(request):
    realisations = Realisation.objects.all()  # Récupérer toutes les réalisations
    return render(request, 'galerie.html', {'realisations': realisations})

def impression_view(resquest):
    return render(resquest,'confirmation.html')

def devis_view(resquest):
    return render(resquest,'devis.html')

def contact_view(resquest):
    return render(resquest,'contact.html')

def dashbord_view(resquest):
    return render(resquest,'dashbord.html')

# realisation 

from django.shortcuts import render, redirect
from .models import Realisation
from .forms import RealisationForm
from django.shortcuts import render, get_object_or_404, redirect


def add_realisation(request):
    # Si c'est une requête POST, on traite l'ajout d'une réalisation
    if request.method == 'POST':
        form = RealisationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_realisation')  # Redirige pour afficher les nouvelles réalisations
    else:
        form = RealisationForm()

    # Récupérer toutes les réalisations existantes
    realisations = Realisation.objects.all()

    return render(request, 'add_realisation.html', {'form': form, 'realisations': realisations})

def delete_realisation(request, realisation_id):
    realisation = get_object_or_404(Realisation, id=realisation_id)
    
    if request.method == 'POST':
        realisation.delete()
        return redirect('add_realisation')  # Redirige après suppression

    return redirect('add_realisation')  # Redirige si ce n'est pas une requête POST


#impression 

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PrintFileForm
from .models import PrintFile

# Fonction pour uploader un fichier
def upload_file(request):
    if request.method == 'POST':
        form = PrintFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '')
            return redirect('/confirmation/')  # Redirection vers la vue qui liste les fichiers
    else:
        form = PrintFileForm()

    return render(request, 'upload_file.html', {'form': form})

# Fonction pour afficher les fichiers envoyés
def view_files(request):
    files = PrintFile.objects.all()  # Récupérer tous les fichiers uploadés
    return render(request, 'view_files.html', {'files': files})

# Fonction pour supprimer un fichier
def delete_file(request, pk):
    file = get_object_or_404(PrintFile, pk=pk)  # Assurez-vous d'utiliser le bon modèle
    file.file.delete()  # Supprime le fichier physique
    file.delete()  # Supprime l'enregistrement de la base de données
    messages.success(request, '')
    return redirect('view_files')


# Demande de devis

from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import DevisForm
from .models import DevisRequest

def demande_devis(request):
    if request.method == 'POST':
        form = DevisForm(request.POST)
        if form.is_valid():
            # Enregistrer la demande en base de données
            devis_request = DevisRequest(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                description=form.cleaned_data['description']
            )
            devis_request.save()

            # Envoyer un email aux administrateurs
            subject = f"Nouvelle demande de devis de {devis_request.name}"
            message = f"""
            Détails de la demande :
            
            Nom : {devis_request.name}
            Email : {devis_request.email}
            Téléphone : {devis_request.phone}
            Description des besoins : {devis_request.description}
            """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['banditchef87@gmail.com'],  # Adresse e-mail entre guillemets
                fail_silently=False,
            )

            # Ajouter un message de succès
            messages.success(request, "Votre demande de devis a été envoyée avec succès ! Nous vous contacterons bientôt.")
            form = DevisForm()  # Réinitialiser le formulaire après soumission
    else:
        form = DevisForm()

    return render(request, 'demande_devis.html', {'form': form})

def liste_devis(request):
    demandes = DevisRequest.objects.all().order_by('-submitted_at')  # Trier par date
    return render(request, 'liste_devis.html', {'demandes': demandes})
