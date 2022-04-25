from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import delo, Type
from .forms import deloForm


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

class deloCreateView(CreateView):
    template_name = 'planner/create.html'
    form_class = deloForm
    success_url = '/planner/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = Type.objects.all()
        return context




# Create your views here.
