from .settings import MEDIA_DEV_MODE
from django.conf import settings
from django.conf.urls.defaults import *
import re

urlpatterns = patterns('')

if MEDIA_DEV_MODE:
    urlpatterns += patterns('',
        (r'^%s(?P<filename>.+)$'
            % re.escape(settings.MEDIA_URL.lstrip('/')),
         'mediagenerator.views.serve_dev_mode'),
    )
