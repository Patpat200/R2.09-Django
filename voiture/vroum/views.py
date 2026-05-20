from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
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
    Marque = models.Marque.objects.get(pk=id)
    return render(request,"vroum/affiche.html",{"Marque": Marque})


def all(request):
    Marque = list(models.Marque.objects.all())
    return render(request, "vroum/all.html", {"Marque": Marque})


def traitementupdate(request, id):
    marque = get_object_or_404(models.Marque, pk=id)

    if request.method == "POST":
        lform = MarqueForm(request.POST, instance=marque)
        if lform.is_valid():
            lform.save()
            return HttpResponseRedirect("/vroum/")
        else:
            return render(request, "vroum/update.html", {"form": lform, "id": id})
    else:
        lform = MarqueForm(instance=marque)
        return render(request, "vroum/update.html", {"form": lform, "id": id})

def delete(request, id):
    marque = get_object_or_404(models.Marque, pk=id)
    marque.delete()
    return HttpResponseRedirect("/vroum/")







def ajoutmodele(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une

        form = ModeleForm(request)
        if form.is_valid(): # validation du formulaire.
            Modele = form.save() # sauvegarde dans la base
            return render(request,"vroum/affichemodele.html",{"Modele" : Modele}) #

        else:
            return render(request,"vroum/ajoutmodele.html",{"form": form})
    else :
        form = ModeleForm() # création d'un formulaire vide
        return render(request,"vroum/ajoutmodele.html",{"form" : form})


def traitementmodele(request):
    lform = ModeleForm(request.POST)
    if lform.is_valid():
        Modele = lform.save()
        return render(request,"vroum/affichemodele.html",{"Modele" : Modele})
    else:
        return render(request,"vroum/ajoutmodele.html",{"form": lform})

def readmodele(request, id):
    Modele = models.Modele.objects.get(pk=id)
    return render(request,"vroum/affichemodele.html",{"Modele": Modele})


def allmodele(request):
    Modele = list(models.Modele.objects.all())
    return render(request, "vroum/allmodele.html", {"Modele": Modele})


def updatemodele(request, id):
    modele = get_object_or_404(models.Modele, pk=id)

    if request.method == "POST":
        lform = ModeleForm(request.POST, instance=modele)
        if lform.is_valid():
            lform.save()
            return HttpResponseRedirect("/vroum/2")
        else:
            return render(request, "vroum/updatemodele.html", {"form": lform, "id": id})
    else:
        lform = ModeleForm(instance=modele)
        return render(request, "vroum/updatemodele.html", {"form": lform, "id": id})

def deletemodele(request, id):
    modele = get_object_or_404(models.Modele, pk=id)
    modele.delete()
    return HttpResponseRedirect("/vroum/2")