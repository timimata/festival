from django.shortcuts import render
from .models import Palco
from .models import Dia
from .models import Concerto


def index_view(request):
    return render(request, 'festival/index.html')


def dias_view(request):
    dias = Dia.objects.all() 

    context = {'dias': dias}

    return render(request, 'festival/dias.html', context)

def palcos_view(request): # criada a função para mostrar os palcos
    palcos = Palco.objects.all() 

    context = {'palcos': palcos} # criada a variavel para passar os palcos para o template

    return render(request, 'festival/palcos.html', context) # criada a função para mostrar os palcos, renderizando o template palcos.html e passando os palcos para o template


def concerto_view(request, id):
    concerto = Concerto.objects.get(id=id)

    context = {'concerto': concerto}

    return render(request, 'festival/concerto.html', context)