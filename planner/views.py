from django.http import HttpResponse

from .models import delo


def index(request):
    s = 'Дела на сегодня:\r\n'
    for simpleDelo in delo.objects:
        s += simpleDelo.title + "\r\n" + simpleDelo.content + '\r\n' + "Важность -" + simpleDelo.importance + "\r\n"
    return HttpResponse(s, content_type='text/plain')

# Create your views here.
