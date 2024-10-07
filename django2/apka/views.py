from django.shortcuts import render, HttpResponse
from .models import model1, model2

# Create your views here.
def views1(request):
    wartosc_z_db = model1.objects.all()
    return render(request,'index.html', context={"zmienna": wartosc_z_db})

def views2(request, id):
    wartosc_pojedyncza_z_db = model2.objects.get(id=id)
    return HttpResponse(f"{wartosc_pojedyncza_z_db.name} / {wartosc_pojedyncza_z_db.location}")