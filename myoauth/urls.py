# -*- coding: utf-8 -*-
from django.conf import urls
from advonl import views

import oauth2client.contrib.django_util.site as django_util_site


urlpatterns = [
    urls.url(r'^$', views.index),
    urls.url(r'^logout$', views.logout),
    # urls.url(r'^profile_required$', views.get_profile_required),
    # urls.url(r'^profile_enabled$', views.get_profile_optional),
    urls.url(r'^oauth2/', urls.include(django_util_site.urls))
]
