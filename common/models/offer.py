import datetime

from django.db import models


__all__ = [
    'Offer',
    'OfferType',
    'OfferStatus'
]


class OfferStatus(models.Model):
    """
    Offer status model.

    Each offer must have a status.
    """
    code: str = models.CharField(max_length=15, primary_key=True)
    description: str = models.CharField(max_length=25)

    class Meta:
        db_table = 'wm_offer_status'
        managed = False


class OfferType(models.Model):
    """
    Offer type model.

    Each offer must have a type.
    """
    code: str = models.CharField(max_length=15, null=False, blank=False, unique=True, primary_key=True)
    description: str = models.CharField(max_length=25)

    class Meta:
        """
        This table is not managed by the app.
        """
        db_table = 'wm_offer_type'
        managed = False


class Offer(models.Model):
    """
    Offer model.
    """
    id: int = models.AutoField(primary_key=True)
    t: models.ForeignKey(OfferType, on_delete=models.CASCADE)
    title: str = models.CharField(max_length=250, null=False, blank=False)
    description: str = models.CharField(max_length=500, null=False, blank=False)
    settings: str = models.CharField(max_length=1000, null=False, blank=False)
    creation_date: datetime.datetime = models.DateTimeField(auto_now_add=True)
    status: OfferStatus = models.ForeignKey(OfferStatus, on_delete=models.CASCADE)
    start_date: datetime.datetime = models.DateTimeField()
    end_date: datetime.datetime = models.DateTimeField()

    class Meta:
        db_table = 'wm_offer'
        managed = False

