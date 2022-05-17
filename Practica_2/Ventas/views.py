from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'Ventas/index.html')

def home(request):
    return render(request,'Ventas/home.html')

def mascota(request):
    contexto= { "nombreM":"ayudante de santa" , "edadM":"2 años" , "colorP":"castaño" , "imagenM":" /static/Ventas/img/pet1.jpeg"}
    return render(request,'Ventas/mascota.html', contexto)    


