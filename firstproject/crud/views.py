from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from . import models

# Create your views here.

def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une

        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            Livre = form.save() # sauvegarde dans la base
            return render(request,"crud/affiche.html",{"Livre" : Livre}) #

        else:
            return render(request,"crud/ajout.html",{"form": form})
    else :
        form = LivreForm() # création d'un formulaire vide
        return render(request,"crud/ajout.html",{"form" : form})


def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request,"crud/affiche.html",{"Livre" : Livre})
    else:
        return render(request,"crud/ajout.html",{"form": lform})


def read(request, id):
    Livre = models.Livre.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"crud/affiche.html",{"Livre": Livre})


def traitementupdate(request, id):
    lform = LivreForm(request.POST)

    if lform.is_valid():
        Livre = lform.save(commit=False)
        Livre.id = id;
        Livre.save()
        return HttpResponseRedirect("/crud/")
    else:
        return render(request, "crud/update.html", {"form": lform, "id": id})

def all(request):
    livres = list(models.Livre.objects.all())
    return render(request, "crud/all.html", {"livres": livres})
