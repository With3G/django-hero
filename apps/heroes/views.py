from django.shortcuts import render, redirect

from .models import *


def index(request):
    """
    -- LIST --
    :param request:
    :return:
    """

    heroes = Hero.objects.all()

    return render(request, 'heroes/index.html', {
        'heroes': heroes
    })


def create(request):
    """
    -- CREATE --
    :param request:
    :return:
    """
    return render(request, 'heroes/create.html')


def read(request, id):
    """
    -- READ --
    :param request:
    :param id:
    :return:
    """
    return render(request, 'heroes/read.html')


def update(request, id):
    """
    -- UPDATE --
    :param request:
    :param id:
    :return:
    """
    return render(request, 'heroes/update.html')


def delete(request, id):
    """
    -- DELETE --
    :param request:
    :param id:
    :return:
    """
    return redirect('heroes:index')
