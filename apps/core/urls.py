from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [

    # ex: modal_confirm_action/
    path('modal_confirm_action/', views.modal_confirm_action),
]
