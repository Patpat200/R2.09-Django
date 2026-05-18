from django.shortcuts import render
from . import models
from .forms import MarqueForm
from .forms import ModeleForm


# Create your views here.
def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une

        form = MarqueForm(request)
        if form.is_valid(): # validation du formulaire.
            Marque = form.save() # sauvegarde dans la base
            return render(request,"vroum/affiche.html",{"Marque" : Marque}) #

        else:
            return render(request,"vroum/ajout.html",{"form": form})
    else :
        form = MarqueForm() # création d'un formulaire vide
        return render(request,"vroum/ajout.html",{"form" : form})


def traitement(request):
    lform = MarqueForm(request.POST)
    if lform.is_valid():
        Marque = lform.save()
        return render(request,"vroum/affiche.html",{"Marque" : Marque})
    else:
        return render(request,"vroum/ajout.html",{"form": lform})


def read(request, id):
    Marque = models.Marque.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"vroum/affiche.html",{"Marque": Marque})


def all(request):
    Marque = list(models.Marque.objects.all())
    return render(request, "vroum/all.html", {"Marque": Marque})

