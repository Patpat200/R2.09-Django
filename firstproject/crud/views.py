from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from django.shortcuts import get_object_or_404
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
    # On récupère le livre existant ou on renvoie une erreur 404 s'il n'existe pas
    livre = get_object_or_404(models.Livre, pk=id)

    if request.method == "POST":
        # On lie le formulaire aux données envoyées (POST) ET à l'instance existante
        lform = LivreForm(request.POST, instance=livre)
        if lform.is_valid():
            lform.save() # Sauvegarde les modifications
            return HttpResponseRedirect("/crud/")
        else:
            return render(request, "crud/update.html", {"form": lform, "id": id})
    else:
        # Cas GET : On affiche le formulaire pré-rempli avec les infos du livre
        lform = LivreForm(instance=livre)
        return render(request, "crud/update.html", {"form": lform, "id": id})

def all(request):
    livres = list(models.Livre.objects.all())
    return render(request, "crud/all.html", {"livres": livres})


def delete(request, id):
    livre = get_object_or_404(models.Livre, pk=id)
    livre.delete()
    return HttpResponseRedirect("/crud/") # Redirection vers la liste après suppression