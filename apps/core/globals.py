from django.conf import settings


def base(request):
    """
    Función que convierte las variables declaradas en conf/settings/base a variables accesibles en los templates
    Ojo: esta funccion es similar que core/permissions.py/base
    :param request:
    :return:
    """
    return {
        'APP_NAME': settings.APP_NAME,
        'PREFIX_DEFAULT_LANGUAGE': settings.PREFIX_DEFAULT_LANGUAGE,
        'BASE_URL': get_base_url(request)
    }


def get_base_url(request):
    """
    Función que devuelve la BASE_URL para los AJAX
    :param request: object
    :return:        'http://localhost:8001/es' | 'http://localhost:8001'
    """
    # protocol = ''.join(['http', 's' if request.is_secure() else '', ':/'])                  # http:// | https://
    protocol = ''.join(['http', 's' if getattr(settings, 'USE_HTTPS', False) else '', ':/'])  # http:// | https://
    host = request.get_host()                                                                 # localhost:8001
    lang = request.LANGUAGE_CODE if settings.PREFIX_DEFAULT_LANGUAGE else None                # es | None

    return '/'.join([protocol, host, lang] if lang else [protocol, host])                     # http://localhost:8001/es
