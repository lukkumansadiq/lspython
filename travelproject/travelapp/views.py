from django.shortcuts import render
from . models import Place, Team
# Create your views here.
from django.http import HttpResponse

def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render (request, 'index.html', {'result' : obj, 'result1' : obj1})

def about(request):
    return render (request, 'about.html')
def contact(request):
    return render (request, 'contact.html')

