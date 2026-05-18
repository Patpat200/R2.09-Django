from django.db import models

# Create your models here.
class Marque(models.Model): #déclare la classe Livre héritant de la classe Model, classe
    nom = models.CharField(max_length=100) # défini un champs de type texte de 100

    fondateur = models.CharField(max_length = 100)

    date_creation = models.DateField(blank=True, null = True) # champs de type date

    pays_origine = models.CharField(blank=False) # champs de type entier devant

    resume = models.TextField(null = True, blank = True) # champs de type text long

    def __str__(self):
        chaine = f"{self.nom} fondé par {self.fondateur}, créer en {self.date_creation} en {self.pays_origine}"
        return chaine


class Modele(models.Model): #déclare la classe Livre héritant de la classe Model, classe

    nom = models.CharField(max_length=100) # défini un champs de type texte de 100

    energie = models.CharField(max_length = 100)

    nombre_chevaux = models.IntegerField(blank=True, null = True) # champs de type date

    type_moteur = models.CharField(blank=False) # champs de type entier devant

    prix = models.IntegerField(blank=False) # champs de type entier devant

    marque = models.ForeignKey("Marque", on_delete=models.CASCADE, default=None)

    resume = models.TextField(null = True, blank = True) # champs de type text long

    def __str__(self):
        chaine = f"{self.nom}, {self.energie}, {self.nombre_chevaux}ch, {self.type_moteur}, {self.prix}€, de {self.marque}"
        return chaine