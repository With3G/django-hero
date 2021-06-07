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

