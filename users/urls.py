from django.urls import include, path
from . import views

urlpatterns = [
    path('signup',views.add,name="signup"),
    path('signin',views.login,name="signin"),
    path('logout',views.logout,name='logout')
    # path('delete/<str:id>')
    
]
