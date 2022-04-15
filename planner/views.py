from django.http import HttpResponse
from django.template import  loader

from .models import delo


def index(request):
    template = loader.get_template('planner/index.html')
    delos = delo.objects.all()
    context = {'delos': delos}
    return HttpResponse(template.render(context, request))


# Create your views here.
