from django.urls import path
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.decorators import csrf
from django.views.decorators import http


@csrf.csrf_exempt
@http.require_POST
def register(request: HttpRequest) -> HttpResponse:
    """
    Register a new user.

    :param request: http request
    :return: 200 OK, 400 Bad Request, 500 Internal Server Error
    """
    pass


@csrf.csrf_exempt
@http.require_POST
def login(request: HttpRequest) -> HttpResponse:
    """
    Login an existing user.

    :param request: http request
    :return: 200 OK, 400 Bad Request, 401 Unauthorized, 500 Internal Server Error
    """
    pass


@csrf.csrf_exempt
@http.require_http_methods(['DELETE'])
def logout(request: HttpRequest) -> HttpResponse:
    pass


urls = [
    path('/v1/user/register', register),
    path('/v1/user/login', login),
    path('/v1/user/logout', logout)
]
