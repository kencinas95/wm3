import typing
import logging
import functools

from django.conf import settings
from django.http import HttpRequest
from django.http import HttpResponseForbidden
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from administrator.models import AdminUser, AdminSession
from administrator.models import AdminProfile
from administrator.service import security


log = logging.getLogger('wm.admin.service.administrator')


def create(username: str,
           raw_password: str,
           profile_code: str,
           name: str,
           surname: str,
           email: str,
           phone: int) -> AdminUser:
    """
    Creates a new Administrator User

    :param username: unique username
    :param raw_password: plain text password
    :param profile_code: profile raw code
    :param name: administrator name
    :param surname: administrator surname
    :param email: administrator email
    :param phone: administrator phone
    :return: new AdminUser instance
    """

    log.info(f"Creating a new user: {username}, {raw_password}, {profile_code}, {name}, {surname}, {email}, {phone}")

    pepper = security.generate_pepper_for_administrator(username)
    password = security.generate_secure_password(raw_password, settings.SECRET_KEY, pepper)

    try:
        profile = AdminProfile.objects.get(code=profile_code)
    except AdminProfile.DoesNotExist as dne:
        log.exception("Could not create new user.")
        raise dne

    try:
        validate_email(email)
    except ValidationError as ve:
        log.exception("Could not create new user.")
        raise ve

    user = AdminUser()
    user.username = username
    user.password = password
    user.pepper = pepper
    user.profile = profile
    user.name = name
    user.surname = surname
    user.email = email
    user.phone = phone

    user.save()
    return user


def login(username: str, raw_password: str) -> (str, AdminUser):
    """
    Login administrator.

    :param username: username
    :param raw_password: plain text password
    :return: session token & user
    """
    log.info(f"Logging in administrator: {username}")

    user = AdminUser.objects.get(username=username)
    password = security.generate_secure_password(raw_password, settings.SECRET_KEY, user.pepper)
    if user.password != password:
        log.error(f'Password missmatch for administrator {username}')
        raise ValueError('password')

    # Delete all user sessions
    AdminSession.objects.filter(user=user).delete()

    while True:
        sid = security.generate_sid(user.username, settings.SECRET_KEY, user.pepper)
        try:
            AdminSession.objects.get(sid=sid, user=user)
        except AdminSession.DoesNotExist:
            session = AdminSession()
            session.sid = sid
            session.user = user
            session.save()
            break

    return session.sid, user


def required_session(func: typing.Callable):
    @functools.wraps(func)
    def wrap(request: HttpRequest, *args, **kwargs):
        if not request.session:
            return HttpResponseForbidden()
        if 'sid' not in request.session:
            return HttpResponseForbidden()
        if 'user' not in request.session:
            return HttpResponseForbidden()
    return wrap
