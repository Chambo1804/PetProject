from django.urls import path

from .views import index, by_type, deloCreateView

urlpatterns = [
    path ('<int:type_id>/', by_type, name='by_type'),
    path ('add/', deloCreateView.as_view(), name='add'),
    path ('', index, name='index'),
]