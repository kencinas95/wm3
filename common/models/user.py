import typing
import datetime

from django.db import models

from common.models.payment import PaymentType


__all__ = [
    'Contact',
    'ContactType',
    'ContactStatus',
    'Gender',
    'User',
    'UserTier',
    'UserStatus',
    'UserActivation',
    'Session'
]


class ContactStatus(models.Model):
    """
    User's contact status model.

    Each contact must have a status.
    """
    code: str = models.CharField(max_length=15, primary_key=True)
    description: str = models.CharField(max_length=15)

    class Meta:
        """
        This table is not managed by the app.
        """
        db_table = 'wm_user_contact_status'
        managed = False


class ContactType(models.Model):
    """
    User's contact type model.

    Each user's contact model must have a type.
    """
    code: str = models.CharField(max_length=15, primary_key=True)
    description: str = models.CharField(max_length=50)

    class Meta:
        """
        This table is not managed by the app.
        """
        db_table = 'wm_user_contact_type'
        managed = False


class Gender(models.Model):
    """
    User's gender model.

    Each user must have a gender.
    """
    code: str = models.CharField(max_length=3, primary_key=True)
    description: str = models.CharField(max_length=25, unique=True, blank=False, null=False)

    class Meta:
        db_table = 'wm_user_gender'
        managed = False


class UserStatus(models.Model):
    """
    User's status model.

    Each user must have a valid status.
    """
    code: str = models.CharField(max_length=15, primary_key=True)
    description: str = models.CharField(max_length=50, unique=True, blank=False, null=False)

    class Meta:
        """
        This table is not managed by the app.
        """
        db_table = 'wm_user_status'
        managed = False


class UserTier(models.Model):
    """
    User's tier model.

    Each user have a tier.
    """
    code: str = models.CharField(max_length=15, unique=True, primary_key=True)
    base_points: int = models.IntegerField()
    next_tier_points: int = models.IntegerField()

    class Meta:
        """
        This table is not managed by the app.
        """
        db_table = 'wm_user_tier'
        managed = False


class User(models.Model):
    """
    User model.
    """
    uid: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=100)
    surname: str = models.CharField(max_length=100)
    username: str = models.CharField(max_length=250, unique=True, blank=False, null=False)
    password: str = models.CharField(max_length=128)
    pepper: str = models.CharField(max_length=128)
    status: UserStatus = models.ForeignKey(UserStatus, on_delete=models.CASCADE)
    gender: Gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    birth_date: datetime.datetime = models.DateField()
    created_at: datetime.datetime = models.DateTimeField(auto_now_add=True)
    last_login: datetime.datetime = models.DateTimeField(auto_now=True)
    news_feed: bool = models.BooleanField()
    tier: UserTier = models.ForeignKey(UserTier, on_delete=models.CASCADE)
    tier_points: int = models.IntegerField()
    payments: typing.Set[PaymentType] = models.ManyToManyField(PaymentType)

    class Meta:
        db_table = 'wm_user'
        managed = False


class UserActivation(models.Model):
    """
    User's activation model.

    When registering a new user, that one must be activated.
    """
    code: str = models.CharField(max_length=128, primary_key=True)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at: datetime.datetime = models.DateTimeField(auto_now_add=True)
    activated_at: datetime.datetime = models.DateTimeField()

    class Meta:
        db_table = 'wm_user_activation'
        managed = False


class Session(models.Model):
    """
    User's session model.
    """
    sid: str = models.CharField(max_length=256, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expires = models.DateTimeField()

    class Meta:
        db_table = 'wm_user_session'
        managed = False


class Contact(models.Model):
    """
    User's contact model.

    Each user must have at least 1 contact, and one of them must be an email.
    """
    id: int = models.AutoField(primary_key=True)
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    t: ContactType = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    value: str = models.CharField(max_length=250, null=False, blank=False)
    status: ContactStatus = models.ForeignKey(ContactStatus, on_delete=models.CASCADE)
    is_main: bool = models.BooleanField()

    class Meta:
        db_table = 'wm_user_contact'
        managed = False


