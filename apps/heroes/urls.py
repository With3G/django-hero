from django.urls import path, include

from . import views

app_name = 'heroes'
urlpatterns = [

    path('', include(([
        path('', views.index, name='index'),
        path('<int:id>', views.read, name='read'),
        path('create/', views.create, name='create'),
        path('update/<int:id>', views.update, name='update'),
        path('delete/<int:id>', views.delete, name='delete'),
    ]))),
]
