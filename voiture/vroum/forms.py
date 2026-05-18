from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class MarqueForm(ModelForm):
    class Meta:
        model = models.Marque
        fields = ('nom', 'fondateur', 'date_creation', 'pays_origine','resume')
        labels = {
            'nom' : _('Nom'),
            'fondateur' : _('Fondateur') ,
            'date_creation' : _('Date de creation'),
            'pays_origine' : _("Pays d'origine"),
            'resume' : _('Résumé')
        }


class ModeleForm(ModelForm):
    class Meta:
        model = models.Modele
        fields = ('nom', 'energie', 'nombre_chevaux', 'type_moteur','prix','marque','resume')
        labels = {
            'nom' : _('Nom'),
            'energie' : _('Energie') ,
            'nombre_chevaux' : _('Nombre de chevaux'),
            'type_moteur' : _('Type de moteur'),
            'prix': _('Prix'),
            'marque': _('Marque'),
            'resume' : _('Résumé')
        }


# python manage.py makemigrations vroum
# python manage.py migrate