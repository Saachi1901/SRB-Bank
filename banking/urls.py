from django.urls import path
from . import views

urlpatterns = [
    
    #path("",views.index,name='index'),
    path("",views.home,name='home'),
    path("customers/",views.customers,name='customers'),
    path("history",views.history,name='history'),
    path("next/<int:mid>",views.next,name='next'),
]