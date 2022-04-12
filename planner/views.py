from django.http import HttpResponse

from .models import delo


def index(request):
    s = 'Дела на сегодня:\r\n'
    for simpleDelo in delo.objects.all():
        s += simpleDelo.title + "\r\n" + simpleDelo.content + '\r\n' + "Важность -" + str(simpleDelo.importance) + "\r\n"
    return HttpResponse(s, content_type='text/plain; charset=utf-8')

# Create your views here.
