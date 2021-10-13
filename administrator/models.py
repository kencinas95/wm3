import datetime

from django.db import models


class AdminProfile(models.Model):
    """
    [KEY-VALUE table] Admin Profile for admin users.
    """
    code: str = models.CharField(max_length=32, primary_key=True, unique=True, blank=False, null=False)
    description: str = models.CharField(max_length=64, unique=True, blank=False, null=False)
    is_superuser: bool = models.BooleanField(default=False)

    class Meta:
        db_table = 'wm_admin_profile'


class AdminPermission(models.Model):
    """
    Admin Permission for tables managed by profile.
    """
    code: int = models.AutoField(primary_key=True)
    profile = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
    table: str = models.CharField(max_length=128, blank=False, null=False)
    allow_select: bool = models.BooleanField()
    allow_insert: bool = models.BooleanField()
    allow_update: bool = models.BooleanField()
    allow_delete: bool = models.BooleanField()

    class Meta:
        db_table = 'wm_admin_permission'


class AdminUser(models.Model):
    """
    Admin User for the app.
    """
    username: str = models.CharField(max_length=128, primary_key=True, unique=True, blank=False, null=False)
    password: str = models.CharField(max_length=128, blank=False, null=False)
    profile: AdminProfile = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
    pepper: str = models.CharField(max_length=64, blank=False, null=False)
    name: str = models.CharField(max_length=128, blank=False, null=False)
    surname: str = models.CharField(max_length=128, blank=False, null=False)
    email: str = models.EmailField()
    phone: int = models.PositiveBigIntegerField()

    class Meta:
        db_table = 'wm_admin_user'


class AdminSession(models.Model):
    """
    Admin Session
    """
    sid: str = models.CharField(max_length=128, primary_key=True, unique=True, blank=False, null=False)
    user: AdminUser = models.ForeignKey(AdminUser, on_delete=models.CASCADE, unique=True)
    since: datetime.datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'wm_admin_session'

