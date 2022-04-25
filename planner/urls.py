from django.urls import path

from .views import index, by_type

urlpatterns = [
    path ('<int:type_id>/', by_type, name ='by_type'),
    path ('', index, name = 'index'),
]