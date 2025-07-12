from django.db import models

class Utilisateur(models.Model):
    # SEXE_CHOICES = [
    #     ('H', 'Homme'),
    #     ('F', 'Femme'),
    #     ('A', 'Autre'),
    # ]

    prenom = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    date_naissance = models.DateField()
    
    mail = models.EmailField(max_length=50, unique=True)  # Champ email avec validation + unicité
    password = models.CharField(max_length=128)  # Prévois de hasher le mot de passe avec make_password

    phone = models.CharField(max_length=15)  # max_length élargi pour gestion internationale
    domaine = models.CharField(max_length=40)

    profile = models.ImageField(upload_to='profiles/', default='profiles/profile.png')

    adresse = models.CharField(max_length=100)

    ville = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)

    sexe = models.CharField(max_length=1)

    ami = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.mail}"
