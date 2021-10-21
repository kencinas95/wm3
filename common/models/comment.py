import datetime

from django.db import models

from common.models.item import Item
from common.models.user import User


__all__ = [
    'Comment',
    'Complain',
    'ComplainStatus'
]


class Comment(models.Model):
    """
    Comment model.
    """
    comment_id: int = models.AutoField(primary_key=True)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    item: Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    message: str = models.CharField(max_length=250, blank=False, null=False)
    liked: bool = models.BooleanField(null=True)
    created_at: datetime.datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'wm_comment'
        managed = False


class ComplainStatus(models.Model):
    """
    Complain status model.

    Each complain must have a status.
    """
    code: str = models.CharField(max_length=15, primary_key=True)
    description: str = models.CharField(max_length=50)

    class Meta:
        """
        This table is not managed by the app.
        """
        db_table = 'wm_comment_complain_status'
        managed = False


class Complain(models.Model):
    """
    Complain model.
    """
    id: int = models.AutoField(primary_key=True)
    code: str = models.CharField(max_length=128)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    message: str = models.CharField(max_length=500, blank=False, null=False)
    created_at: datetime.datetime = models.DateTimeField(auto_now_add=True)
    replied_at: datetime.datetime = models.DateTimeField(auto_now=True)
    status: ComplainStatus = models.ForeignKey(ComplainStatus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wm_comment_complain'
        managed = False

