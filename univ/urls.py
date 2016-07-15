from django.conf.urls import url
from . import views

app_name = 'univ'

urlpatterns = [
    # facultad/Fa22
    url(r'^facultad/(?P<facu_id>[a-zA-Z0-9]+)/$', views.facu_detalles, name='facu_detalles'),
    url(r'^$', views.index, name='index'),
]
