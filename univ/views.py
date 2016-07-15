from django.shortcuts import render, redirect
from django.http import Http404
# for json data retrieve
import urllib.request as ur
import json
# for fb logout
from django.contrib.auth import logout


def index(request):
    #facu
    url = 'http://52.36.38.235:9988/facultades'
    html = ur.urlopen(url).read()
    all_facus = json.loads(html.decode('utf-8'))

    #noticias
    url = 'http://52.36.38.235:9988/noticias'
    html = ur.urlopen(url).read()
    all_news = json.loads(html.decode('utf-8'))

    context = {
        'all_facus': all_facus,
        'all_news': all_news,
    }
    return render(request, 'univ/facus.html', context)


def facu_detalles(request, facu_id):
    #facultad
    url = 'http://52.36.38.235:9988/facultades/' + str(facu_id)
    html = ur.urlopen(url).read()
    facultad = json.loads(html.decode('utf-8'))

    #escuelas
    # url = 'http://52.36.38.235:9988/escuelas'
    # html = ur.urlopen(url).read()
    # all_escuelas = json.loads(html.decode('utf-8'))

    if facultad['Id']:
        return render(request, 'univ/facu_detalles.html', {'facultad': facultad})
    else:
        raise Http404("Facultad inexistente")

# fb logout
def LogOut(request):
    logout(request)
    return redirect('/')