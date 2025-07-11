from django.shortcuts import render,redirect
from .models import Utilisateur

# Create your views here.
def inscription(request):
    accepted = True
    
    if request.method == 'POST':
        users =  Utilisateur.objects.all()
        data  = request.POST
        
        prenom = data.get('prenom')
        nom = data.get('nom')
        
        date_naissance = data.get('naissance')
        mail = data.get('email')
        
        password = data.get('password')
        phone = data.get('telephone')
        
        domaine = data.get('domaine')
        profile = data.get('profile')
        
        adresse = data.get('adresse')
        ville = data.get('ville')
        pays  = data.get('pays')
        
        genre = data.get('genre')    
        
        conditions = data.get('conditions')  
        
        if conditions :
            for user in users :
                if user.password == password  or user.mail == mail or not profile:
                    accepted = False
                    
        if accepted:
            user = Utilisateur(prenom = prenom,nom = nom,
                               date_naissance = date_naissance,mail = mail ,
                               password = password,phone = phone,
                               domaine = domaine,profile = profile,
                               adresse = adresse,ville = ville,
                               pays =  pays,sexe = genre,)
            user.save()
            return redirect('connexion')
    
    
    
    return render(request,'users/inscription.html')

def  connexion(request):
    request.session['logged_user_id'] = None
    connected = False
    if request.method == 'POST':
        data = request.POST
        mail = data.get('email')
        password = data.get('password')
        
        users =  Utilisateur.objects.all()
        for user in users :
            if user.mail == mail and user.password == password :
                request.session['logged_user_id'] = user.id
                connected = True
        if connected:
            return redirect('home/')
    
    return render(request,'users/connexion.html')