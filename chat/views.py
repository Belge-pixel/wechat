from django.shortcuts import render
from users.models import Utilisateur
from chat.models import Message
from django.db.models import Q

# Create your views here.
def chat(request,friend_id):
    send = True
    
    if 'logged_user_id'  in request.session  or request.method == 'POST':
        
        data = request.POST
        
        contenu  = data.get('message')
        
        user =  Utilisateur.objects.get(id  = request.session['logged_user_id'])
        friend =  Utilisateur.objects.get(id  = friend_id)
        
        messages = Message.objects.filter(
    Q(expediteur=user, destinataire=friend) |
    Q(expediteur=friend, destinataire=user)
        ).order_by('date') 
        
        if contenu :
            my_message = Message(contenu = contenu,expediteur = user ,destinataire = friend)
            
            for message in messages:
                if message.contenu == my_message.contenu  :
                    send = False
            if send:        
                my_message.save()
      
        
        return render(request,'chat/index.html',{'user':user,'friend':friend,'messages':messages})
    
    
    return render(request,'chat/index.html')