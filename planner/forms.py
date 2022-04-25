from django.forms import ModelForm

from .models import delo

class deloForm(ModelForm):
    class Meta:
        model = delo
        fields = {'title', 'content', 'time', 'importance', 'type'}