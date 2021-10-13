from django.db import models


__all__ = [
    'PaymentType'
]


class PaymentType(models.Model):
    """
    Payment type model.

    Each user has at least one payment type.
    """
    code: str = models.CharField(max_length=10, primary_key=True)
    description: str = models.CharField(max_length=50)
    enabled: bool = models.BooleanField()

    class Meta:
        db_table = 'wm_payment_type'

