from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import delo, Type


def index(request):
    delos = delo.objects.all()
    types = Type.objects.all()
    context = {'delos':delos, 'types':types}
    return render(request, 'planner/index.html', context)

def by_type(request, type_id):
    delos = delo.objects.filter(type=type_id)
    types = Type.objects.all()
    current_type = Type.objects.get(pk=type_id)
    context = {'delos': delos, 'types': types, 'current_type': current_type}
    return render(request, 'planner/by_type.html', context)



# Create your views here.
