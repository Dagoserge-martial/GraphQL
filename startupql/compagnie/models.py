from django.db import models

# Create your models here.

# City where employees live
class Ville(models.Model):
    name = models.CharField(max_length=100)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Employee title
class Titre(models.Model):
    name = models.CharField(max_length=100)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employe(models.Model):
    name = models.CharField(max_length=255)
    ville = models.ForeignKey(Ville,  on_delete=models.CASCADE, related_name='ville_emplye' )
    titre = models.ForeignKey(Titre,  on_delete=models.CASCADE, related_name='titre_emplye' )

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.name

#python manage.py seed compagnie --number=15
#python manage.py admin_generator compagnie >> compagnie/admin.py