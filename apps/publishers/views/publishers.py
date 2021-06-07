from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages

from ..forms.publishers import PublisherForm
from ...publishers.models import Publisher


def index(request):
    """
    -- LIST --
    :param request:
    :return:
    """

    publishers = Publisher.objects.all()

    return render(request, 'publishers/index.html', {
        'publishers': publishers
    })


def read(request, id):
    """"
    -- READ --
    :param request:
    :param id:
    :return:
    """

    try:
        publisher = Publisher.objects.get(pk=id)
    except Publisher.DoesNotExist:
        raise Http404(_('Publisher not exist'))

    return render(request, 'publishers/read.html', {
        'publisher': publisher
    })


def create(request):
    """
    -- CREATE --
    :param request:
    :return:
    """

    form = PublisherForm()

    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, _('Configuración guardada con éxito.'), extra_tags='fadeOut')
            return redirect('publishers:index')

    return render(request, 'publishers/create.html', {
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
        publisher = Publisher.objects.get(pk=id)
    except Publisher.DoesNotExist:
        raise Http404(_('Publisher not exist'))

    form = PublisherForm(instance=publisher)

    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, _('Configuración guardada con éxito.'), extra_tags='fadeOut')
            return redirect('publishers:index')

    return render(request, 'publishers/update.html', {
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
        publisher = Publisher.objects.get(pk=id)
    except Publisher.DoesNotExist:
        raise Http404(_('Publisher not exist'))

    publisher.delete()
    messages.success(request, _('Configuración guardada con éxito.'), extra_tags='fadeOut')

    return redirect('publishers:index')


