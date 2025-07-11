from django.shortcuts import render
from users.models import Utilisateur
from blog.models import Publication
from .forms import*
from .models import*

# Create your views here.
def blog(request):
    
    if 'logged_user_id'  in request.session :
        user = Utilisateur.objects.get(id = request.session['logged_user_id'])
        # pubs = Publication.objects.filter(auteur__ami = user)

        if request.method == 'POST':
            data = request.POST

            titre = data.get('titre')
            content =  data.get('contenu')
            image = data.get('fichier')

            pub = Publication(titre = titre,contenu = content , image = image , auteur = user)
            pub.save()
        
        pubs = Publication.objects.filter(
    models.Q(auteur__ami=user) | models.Q(auteur=user)
).distinct()

        form  = PubForm()
        if user:
            data = {'form':form,'user':user,'pubs':pubs}
            return render(request,'blog/index.html',context =data)
            
    return render(request,'users/inscription.html')
    


def detail(request,slug):
    article = Publication.objects.filter(titre = slug).first()
    user = Utilisateur.objects.get(id = request.session['logged_user_id'])


    return render(request,'blog/detail.html',{'article':article,'user':user})    