
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),

    path('marque/ajout/', views.ajout),
    path('marque/traitement/', views.traitement),
    path('marque/affiche/<int:id>/', views.read),
    path('marque/', views.all),
    path('marque/update/<int:id>/', views.traitementupdate),
    path('marque/delete/<int:id>/', views.delete),


    # path('affichemodele/<int:id>/', views.readmodele),
    path('modele/ajoutmodele/', views.ajoutmodele),
    path('modele/traitementmodele/', views.traitementmodele),
    path('modele/', views.allmodele),
    path('modele/updatemodele/<int:id>/', views.updatemodele),
    path('modele/deletemodele/<int:id>/', views.deletemodele),

]