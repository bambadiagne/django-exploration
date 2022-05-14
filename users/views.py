from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password
from todolist_functions_views.models import SimpleUser
from users.forms import UserForm

def add(request):
    if(request.method=="POST"):
        form = UserForm(request.POST)
        if(form.is_valid()):
            name=form.cleaned_data['name']
            password = make_password(form.cleaned_data['password'])
            user=SimpleUser(name=name,password=password)
            user.save()
            request.session['user_id'] = user.pk
            return redirect("/")
        print(form.fields)    
        
        return render(request,"add_user.html",{"form":form})    
    return render(request,"add_user.html",{"form":""})             

def login(request):
    if(request.method=="POST"):
        form = UserForm(request.POST)
        if(form.is_valid()):
            user=SimpleUser.objects.filter(name=form.cleaned_data['name']).first()
            password = form.cleaned_data['password']
            if(user):
                if(check_password(password,user.password)):
                    request.session['user_id'] = user.id
                    return redirect("/")
            form.errors["k"]="Mot de passe insdsd"        
            return render(request,"signin.html",{"error":"Combinaison user + mot de passe introuvable"})        
        return render(request,'signin.html',{'form':form})            
            
    return render(request,'signin.html')    

def logout(request):
    request.session.modified = True
    del request.session["user_id"]
    return redirect("/users/signin")