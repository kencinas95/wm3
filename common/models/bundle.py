import uuid
import datetime

from django.db import models
from django.core.validators import MinValueValidator

from common.models.item import Item


__all__ = [
    'Bundle',
    'BundleGroup'
]


class BundleGroup(models.Model):
    """
    Bundle group model.

    Group of bundles of items.
    """
    id: uuid.UUID = models.UUIDField(primary_key=True)
    creation_date: datetime.datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'wm_bundle_group'


class Bundle(models.Model):
    """
    Bundle model.

    Items are meant to be bundled to create a purchase.
    """
    id: int = models.AutoField(primary_key=True)
    bundle_group: BundleGroup = models.ForeignKey(BundleGroup, on_delete=models.CASCADE)
    total: models.PositiveIntegerField(validators=[MinValueValidator(1)])
    item: Item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wm_bundle'
