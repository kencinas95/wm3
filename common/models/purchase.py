import datetime

from django.db import models

from common.models.user import User
from common.models.bundle import BundleGroup
from common.models.payment import PaymentType


__all__ = [
    'Purchase',
    'PurchaseStatus'
]


class PurchaseStatus(models.Model):
    """
    Purchase status model.

    Each purchase instance must have a status.
    """
    code: str = models.CharField(max_length=25, primary_key=True)
    description: str = models.CharField(max_length=50)

    class Meta:
        """
        This table is not managed by the app.
        """
        db_table = 'wm_purchase_status'
        managed = False


class Purchase(models.Model):
    """
    Purchase model.
    """
    id: int = models.AutoField(primary_key=True)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    payment: PaymentType = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    bundle_group: BundleGroup = models.ForeignKey(BundleGroup, on_delete=models.CASCADE)
    final_price: float = models.FloatField()
    creation_date: datetime.datetime = models.DateField(auto_now_add=True)
    payment_date: datetime.datetime = models.DateField()

    class Meta:
        db_table = 'wm_purchase'
        managed = False

