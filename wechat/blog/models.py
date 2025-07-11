from django.db import models
from users.models import Utilisateur  # Évite le `import *`, trop vague

class Publication(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(max_length=5000)
    
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', default='blog/podcast.jpg')  # Par exemple : un fichier image par défaut
    
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='publications')

    def __str__(self):
        return f"{self.titre} par {self.auteur.prenom}"


class Commentaire(models.Model):
    contenu = models.CharField(max_length=500)
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='commentaires')
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='commentaires')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.auteur.prenom} sur {self.publication.titre}"
