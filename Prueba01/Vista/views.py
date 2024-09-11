from django.shortcuts import render
# Create your views here.

def vistarender(sequest):
    dato = {'nombre':'pablo'}
    return render(sequest,'templatesApp/index.html',dato)