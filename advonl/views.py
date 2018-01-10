# -*- coding: utf-8 -*-
from django import http
from oauth2client.contrib.django_util import decorators
from django.template.response import TemplateResponse


def logout(request):
    request.session.flush()
    return http.HttpResponseRedirect('/')


@decorators.oauth_enabled
def index(request):
    if request.oauth.has_credentials():
        # show logout link too
        return TemplateResponse(
            request,
            'private.html',
            {'credentials': request.oauth.credentials.id_token}
        )
    else:
        return TemplateResponse(
            request,
            'login.html',
            {'redirect': request.oauth.get_authorize_redirect()}
        )
