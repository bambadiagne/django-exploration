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

def update(request,id):
    
    if(request.session.get('user_id')==int(id)):
        current_user=SimpleUser.objects.filter(id=id).first()
        if(request.method=='POST'):
            
            form=UserForm(request.POST)
            if(form.is_valid()):
                SimpleUser.objects.filter(id=id).update(password=make_password(form.cleaned_data['password']),name=form.cleaned_data['name'])
                return redirect("/")
            return render(request,'update_user.html',{'form':form})
        return render(request,"update_user.html",{"current_user":current_user})
    return redirect("/users/signin")
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
            return render(request,"signin.html",{"error":"Combinaison user + mot de passe introuvable"})        
        return render(request,'signin.html',{'form':form})            
            
    return render(request,'signin.html')    

def logout(request):
    request.session.modified = True
    del request.session["user_id"]
    return redirect("/users/signin")