import logging

from django.core import serializers
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from administrator.models import AdminUser

from administrator.service import user as service


log = logging.getLogger('wm.admin.api.user')


def login(request: HttpRequest) -> HttpResponse:
    """
    Login an Administrator User into the backoffice.

    :param request: http request
    :return: http response with session
    """
    try:
        username = str(request.POST['username'])
        password = str(request.POST['password'])

        sid, user = service.login(username, password)
        user_serialized = serializers.serialize('python', [user])[0]['fields']
        user_serialized['username'] = user.username
        user_serialized['profile'] = serializers.serialize('python', [user.profile])[0]['fields']
        user_serialized['profile']['code'] = user.profile.code

        request.session['sid'] = sid
        request.session['user'] = user_serialized

        return redirect('/backoffice', request=request)

    except KeyError:
        log.exception('Could not login user.')
        ctx = {
            'error_msg': 'Could not login user: Missing parameter!'
        }
    except ValueError:
        log.exception('Could not login user.')
        ctx = {
            'error_msg': 'Could not login user: password invalid!'
        }
    except AdminUser.DoesNotExist:
        log.exception('Could not login user.')
        ctx = {
            'error_msg': 'Could not login user: username invalid!'
        }
    return render(request, "administrator/home.html", context=ctx)

