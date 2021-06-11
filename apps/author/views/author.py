from django.http import Http404
from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect
from django.contrib import messages

from apps.author.models import *
from ..forms.author import AuthorForm


def index(request):
    """
    -- LIST --
    :param request:
    :return:
    """

    authors = Author.objects.all()

    return render(request, 'author/index.html', {
        'authors': authors
    })


def create(request):
    """
    -- CREATE --
    :param request:
    :return:
    """
    return render(request, 'author/create.html')


def read(request, id):
    """"
    -- READ --
    :param request:
    :param id:
    :return:
    """

    try:
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        raise Http404(_('Author not exist'))

    return render(request, 'author/read.html', {
        'author': author
    })


def create(request):
    """
    -- CREATE --
    :param request:
    :return:
    """

    form = AuthorForm()

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, _('Configuración guardada con éxito.'), extra_tags='fadeOut')
            return redirect('author:index')

    return render(request, 'author/create.html', {
        'form': form
    })


def update(request, id):
    """"
    -- UPDATE --
    :param request:
    :param id:
    :return:
    """

    try:
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        raise Http404(_('Author not exist'))

    form = AuthorForm(instance=author)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, _('Configuración guardada con éxito.'), extra_tags='fadeOut')
            return redirect('author:index')

    return render(request, 'author/update.html', {
        'form': form
    })


def delete(request, id):
    """"
    -- DELETE --
    :param request:
    :param id:
    :return:
    """

    try:
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        raise Http404(_('Author not exist'))

    author.delete()
    messages.success(request, _('Configuración guardada con éxito.'), extra_tags='fadeOut')

    return redirect('author:index')

