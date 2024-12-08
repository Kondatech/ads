from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('service/', views.service_view),
    path('galerie/', views.galerie),
    path('confirmation/', views.impression_view),
    path('demande-devis/', views.demande_devis, name='demande_devis'),
    path('liste-devis/', views.liste_devis, name='liste_devis'),
    path('contact/', views.contact_view),
    path('admin-dash-ads-key-root/', views.dashbord_view),
    path('ajouter/', views.add_realisation, name='add_realisation'),
    path('supprimer/<int:realisation_id>/', views.delete_realisation, name='delete_realisation'),
    path('upload/', views.upload_file, name='upload_file'),  # URL pour uploader un fichier
    path('view_files/', views.view_files, name='view_files'),  # URL pour voir les fichiers
    path('delete_file/<int:pk>/', views.delete_file, name='delete_file'),  # URL pour supprimer un fichier

]

# Ajouter les fichiers statiques et médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)