from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme
from .forms import FilmeForm
import requests


API_KEY = "d3c3e2ac"

def lista_filmes(request):
    filmes = Filme.objects.all().order_by('titulo')

    media = 0

    if filmes:
        media = sum(f.nota for f in filmes) / len(filmes)

    return render(
        request,
        'lista_filmes.html',
        {
            'filmes': filmes,
            'media': round(media, 2),
            'quantidade': filmes.count()
        }
    )


def adicionar_filme(request):

    if request.method == 'POST':

        titulo = request.POST.get('titulo')
        nota = request.POST.get('nota')

        url = f'https://www.omdbapi.com/?apikey={API_KEY}&t={titulo}'

        resposta = requests.get(url).json()

        print(resposta)

        if resposta.get('Response') == 'True':

            Filme.objects.create(
                titulo=resposta['Title'],
                ano=resposta['Year'],
                diretor=resposta['Director'],
                genero=resposta['Genre'],
                nota=float(nota),
                poster=resposta['Poster']
            )

            return redirect('lista_filmes')

    return render(request, 'adicionar_filme.html')


def editar_filme(request, id):

    filme = get_object_or_404(Filme, id=id)

    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)

        if form.is_valid():
            form.save()
            return redirect('lista_filmes')

    else:
        form = FilmeForm(instance=filme)

    return render(
        request,
        'editar_filme.html',
        {
            'form': form,
            'filme': filme
        }
    )


def excluir_filme(request, id):

    filme = get_object_or_404(Filme, id=id)
    filme.delete()

    return redirect('lista_filmes')