from django.shortcuts import render
from users.models import Utilisateur
from forum.models import Poste

# Create your views here.
def forum(request):
    posted = True


    user = Utilisateur.objects.get(id = request.session['logged_user_id'])
    posts = Poste.objects.all()

    if request.method == 'POST':
        data = request.POST

        content = data.get('contenu')
        post = Poste(contenu = content,auteur = user )

        
        for p in posts:
            if p.auteur.id == user.id and p.contenu ==  content:
                posted = False
        if posted:
            post.save()


    

    return render(request,'forum/index.html',{'user':user,'messages':posts})