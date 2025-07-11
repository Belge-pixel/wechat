from django.db import models
from users.models import Utilisateur  

class Message(models.Model):
    contenu = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_envoyes')
    destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_recus')

    def __str__(self):
        return f"De {self.expediteur.prenom} à {self.destinataire.prenom} le {self.date.strftime('%d/%m/%Y %H:%M')}"
