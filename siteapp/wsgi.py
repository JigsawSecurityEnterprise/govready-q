import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "siteapp.settings")
from django.core.wsgi import get_wsgi_application

django_application = get_wsgi_application()

# Add the MODULES_PATH to the Python modules path so that
# external-function functions can be loaded from Python
# source files near where the functions are used. Add it
# to the end of the path so it can't override build-in
# Python code I guess?
from django.conf import settings
sys.path.append(settings.MODULES_PATH)

if os.getenv('VCAP_APPLICATION'):
    from whitenoise.django import DjangoWhiteNoise
    django_application = DjangoWhiteNoise(django_application)

# WSGI redirect logic from
# https://github.com/GrahamDumpleton/mod_wsgi/issues/86
def application_redirect(environ, start_response, http_host):
    headers = []
    headers.append(('Location', 'https://%s%s%s' % (
            http_host, environ.get('SCRIPT_NAME'),
            environ.get('PATH_INFO'))))
    start_response('302 OK', headers)
    yield ''

def application(environ, start_response):
    http_host = environ.get('HTTP_HOST')

    if (environ.get('wsgi.url_scheme', 'http') != 'https') and os.getenv('VCAP_APPLICATION'):
        return application_redirect(environ, start_response, http_host)
    else:
        return django_application(environ, start_response)