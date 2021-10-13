import typing
import logging
from urllib import parse

from django.http import QueryDict
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotAllowed

from common.models.item import Origin
from common.models.item import OriginCategory


log = logging.getLogger('wm.admin.api.origin')


def create(parameters: typing.Type[QueryDict]) -> typing.NoReturn:
    """
    Creates a new origin by given name and category.

    :param parameters: request body
    :return: new origin
    """
    try:
        name = str(parameters['name'])
        category_pk = str(parameters['origin_category'])
    except KeyError as ke:
        log.error(f"Unable to create origin, missing parameter {ke}")
        raise ke

    log.info(f"Creating new origin: {name}, {category_pk}")
    try:
        category = OriginCategory.objects.get(pk=category_pk)
        origin = Origin.objects.create(name=name, category=category)
        origin.save()
    except OriginCategory.DoesNotExist:
        log.error(f"Unable to create origin, category {category_pk} does not exist.")
        raise ValueError(f"Invalid given category pk: {category_pk}")


def update(parameters: typing.Union[QueryDict, typing.Type[QueryDict]]) -> typing.NoReturn:
    """
    Updates an origin.

    :param parameters:
    :return:
    """
    try:
        pk = int(str(parameters['pk']))
        name = str(parameters['name'])
        category_pk = str(parameters['origin_category'])
    except KeyError as ke:
        log.error(f"Unable to create origin, missing parameter: {ke}")
        raise ke

    log.info(f"Updating {pk} origin: {name}, {category_pk}")
    try:
        origin = Origin.objects.get(pk=pk)
        origin.name = name
        origin.category = OriginCategory.objects.get(pk=category_pk)
        origin.save()
    except Origin.DoesNotExist:
        log.error(f"Unable to update origin, origin {pk} does not exist.")
        raise ValueError(f"Invalid given origin pk: {pk}")
    except OriginCategory.DoesNotExist:
        log.error(f"Unable to update origin, category {category_pk} does not exist.")
        raise ValueError(f"Invalid given category pk: {category_pk}")


def delete(parameters: typing.Union[QueryDict, typing.Type[QueryDict]]) -> typing.NoReturn:
    """
    Deletes an origin.

    :param parameters:
    :return:
    """
    try:
        pk = int(str(parameters['pk']))
    except KeyError as ke:
        log.error(f"Unable to delete origin, missing parameter: {ke}")
        raise ke

    log.info(f"Deleting origin: {pk}")
    try:
        origin = Origin.objects.get(pk=pk)
        origin.delete()
    except Origin.DoesNotExist:
        log.error(f"Unable to delete origin, origin {pk} does not exist.")
        raise ValueError(f"Invalid given origin pk: {pk}")


def handle(request: HttpRequest) -> HttpResponse:
    """
    Handle requests for origin.

    :param request: http request
    :return: http response
    """
    try:
        if request.method.upper() == 'POST':
            create(request.POST)
        elif request.method.upper() == 'PUT':
            parameters = QueryDict(request.body)
            update(parameters)
        elif request.method.upper() == 'DELETE':
            parameters = QueryDict(request.body)
            delete(parameters)
        else:
            log.error(f"Method not allowed for origin handler: {request.method}")
            return HttpResponseNotAllowed(permitted_methods=['POST', 'PUT', 'DELETE'])
    except KeyError as ke:
        return HttpResponseBadRequest(f"missing parameter: {ke}")
    except ValueError as ve:
        return HttpResponseBadRequest(ve)

    return HttpResponse(status=200)
