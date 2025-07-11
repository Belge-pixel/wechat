from django.shortcuts import render,redirect, get_object_or_404
from users.models import Utilisateur
# Create your views here.


def home(request):
    if 'logged_user_id'  in  request.session:
        user_id  = request.session['logged_user_id']
        user = Utilisateur.objects.get(id=user_id)

        print(user)
        
        if user :
            return render(request,'home/index.html',context = {'user':user})
    
    return render(request,'users/connexion.html')

def profile(request,slug):
    
    user = Utilisateur.objects.get(id=slug)
    # user = get_object_or_404(Utilisateur, id=id)


    if user is not None:  
        return render(request,'home/profile.html',context = {'user':user})
    else:
        return redirect('connexion')
    


def amis(request,slug):
    user = Utilisateur.objects.get(id=slug)
    friends = Utilisateur.objects.filter(ami = user)
    
    nb = len(friends)
    
    return render(request,'home/amis.html',{'friends':friends,'nb':nb,'user':user})


def ajouter(request,slug):
    user = Utilisateur.objects.get(id= request.session['logged_user_id']   )
    users = Utilisateur.objects.exclude(id__in=user.ami.values_list('id', flat=True)).exclude(id=user.id)
    if request.method == 'POST':

        print('yes')

        data = request.POST
        users = Utilisateur.objects.exclude(id__in=user.ami.values_list('id', flat=True)).exclude(id=user.id)
        user = Utilisateur.objects.get(id= request.session['logged_user_id'])
        
        if user.id != slug:
            print('oh yes')

            friend = Utilisateur.objects.get(id = slug)
            user.ami.add(friend)
            users = Utilisateur.objects.exclude(id__in=user.ami.values_list('id', flat=True)).exclude(id=user.id)


        return render(request,'home/ajouter.html',{'user':user,'users':users})
    return render(request,'home/ajouter.html',{'user':user,'users':users})    