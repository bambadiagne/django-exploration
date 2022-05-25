from django.shortcuts import redirect, render


def home(request):
    if(not request.session.get('user_id')):
        return redirect("/users/signin")
    return render(request, 'index.html')
