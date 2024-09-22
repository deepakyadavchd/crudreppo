from django.urls import path
from .views import*


urlpatterns = [
    path('create/', createview),
    path('result/', resultview),
    path('details/', detailsview),
    path('delete/', deleteview),
    path('edit/', editview),
    path('signin/', signin),
    path('signup/', signup),
    path('logout/', logoutview),
    path('changepass/', passchange)
        
    


]