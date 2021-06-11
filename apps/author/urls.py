from django.urls import path, include

from .views import author

app_name = 'author'
urlpatterns = [

    path('', include(([
        path('', author.index, name='index'),
        path('<int:id>', author.read, name='read'),
        path('create/', author.create, name='create'),
        path('update/<int:id>', author.update, name='update'),
        path('delete/<int:id>', author.delete, name='delete'),
    ]))),
]