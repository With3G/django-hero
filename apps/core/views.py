from django.utils.translation import ugettext as _
from django.shortcuts import render


def modal_confirm_action(request):
    """
    Función que muestra el modal de confirmación
    :param request:
    :return:
    """

    action_url = action_text = None

    if request.method == 'POST':

        action_url = request.POST.get('action_url', '/')
        action_text = request.POST.get('action_text', _('This action is irreversible, do you want to continue?'))

    print(action_url)
    print(action_text)

    return render(request, 'core/modal_confirm_action.html', {
        'action_url': action_url,
        'action_text': action_text,
    })