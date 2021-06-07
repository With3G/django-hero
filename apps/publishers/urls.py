from django.urls import path, include

from .views import publishers

app_name = 'publishers'
urlpatterns = [

    path('', include(([
        path('', publishers.index, name='index'),
        path('create/', publishers.create, name='create'),
    ]))),
]
