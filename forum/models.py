from django.db import models
from users.models import Utilisateur

# Create your models here.
class Poste(models.Model):
    contenu = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.auteur} - {self.contenu[:30]}..."