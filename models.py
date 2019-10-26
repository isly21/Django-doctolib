
from django.db import models
from django.utils import timezone


class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    dateNaissance = models.DateTimeField()
    adresse = models.CharField(default='rue de la lib',max_length=100)
    
    class Meta:
            verbose_name = "patient"
            ordering = ['date']
        
            def __str__(self):
                """ 
                Cette méthode que nous définirons dans tous les modèles
                nous permettra de reconnaître facilement les différents objets que 
                nous traiterons plus tard dans l'administration    """
                return self.prenom    

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    dateNaissance = models.DateTimeField()
    adresse = models.CharField(default='rue de la lib',max_length=100)
    tarif = models.PositiveSmallIntegerField()