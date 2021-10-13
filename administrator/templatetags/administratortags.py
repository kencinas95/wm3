import json
import typing

from django.db.models import Model
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django import template


register = template.Library()


def jsonify(obj: typing.Union[QuerySet, Model, typing.Any]) -> typing.Any:
    if isinstance(obj, QuerySet):
        result = serialize('python', obj)
    elif isinstance(obj, Model):
        result = serialize('python', [obj])[0]
    else:
        result = json.dumps(obj)
    return result


register.filter('jsonify', jsonify)
jsonify.is_safe = True
