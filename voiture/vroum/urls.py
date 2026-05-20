
from . import views
from django.urls import path

urlpatterns = [
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.read),
    path('', views.all),
    path('update/<int:id>/', views.traitementupdate),
    path('delete/<int:id>/', views.delete),

    path('ajoutmodele/', views.ajoutmodele),
    path('traitementmodele/', views.traitementmodele),
    path('2', views.allmodele),

    path('updatemodele/<int:id>/', views.updatemodele),
    path('deletemodele/<int:id>/', views.deletemodele),

]