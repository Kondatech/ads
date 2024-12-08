from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="Classe CSS pour une icône FontAwesome, ex: fa-paint-brush.")
    image = models.ImageField(upload_to='service/', blank=True, null=True)

    def __str__(self):
        return self.title
    

    # la re lisation 

class Realisation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='galerie/', blank=True, null=True)
    category = models.CharField(max_length=100, choices=[('design', 'Design'), ('impression', 'Impression'), ('peinture', 'Peinture'), ('decoration', 'Décoration')])

    def __str__(self):
        return self.title
    
#impression

from django.db import models

class PrintFile(models.Model):
    PAPER_TYPES = [
        ('Glossy', 'Glossy'),
        ('Matte', 'Matte'),
        ('Standard', 'Standard'),
    ]
    #PRINT_TYPES = [
     #   ('Color', 'Impression couleur'),
      #  ('Black & White', 'Impression noir et blanc'),
    #]

    file = models.FileField(upload_to='uploads/')  # Champ pour le fichier
    name = models.CharField(max_length=255, verbose_name="Nom du client")  # Nom
    client_name = models.CharField(max_length=100, verbose_name="Nom du client")  # Nom du client
    contact = models.CharField(max_length=100, verbose_name="Contact du client")  # Contact
    dimensions = models.CharField(max_length=50, verbose_name="Dimensions  (par ex. 30x40 cm )")  # Dimensions
    paper_type = models.CharField(max_length=20,  verbose_name="type d'impression (par ex. vyle ou bache)")
    print_type = models.CharField(max_length=20,  verbose_name="Nombres d'examplare(Ex: 10)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.file.name}"
    
    # demande de devis 
from django.db import models

class DevisRequest(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Numéro de téléphone")
    description = models.TextField(verbose_name="Description des besoins")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de soumission")

    def __str__(self):
        return f"Demande de devis de {self.name} - {self.email}"
