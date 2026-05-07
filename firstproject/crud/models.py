from django.db import models

# Create your models here.
class Livre(models.Model): #déclare la classe Livre héritant de la classe Model, classe
    titre = models.CharField(max_length=100) # défini un champs de type texte de 100

    auteur = models.CharField(max_length = 100)
    date_parution = models.DateField(blank=True, null = True) # champs de type date

    nombre_pages = models.IntegerField(blank=False) # champs de type entier devant

    resume = models.TextField(null = True, blank = True) # champs de type text long

    def __str__(self):
        chaine = f"{self.titre} écrit par {self.auteur} édité le {self.date_parution}"
        return chaine
