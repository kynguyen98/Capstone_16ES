# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cameralist(models.Model):
    cameraid = models.CharField(primary_key=True, max_length=6)
    parkinglotid = models.ForeignKey(
        'Parkinglotlist', models.DO_NOTHING, db_column='parkinglotid', blank=True, null=True)
    camerabrand = models.CharField(max_length=20, blank=True, null=True)
    cameraspec = models.CharField(max_length=40, blank=True, null=True)
    inorout = models.BooleanField(blank=True, null=True)

    class Meta:
        app_label = 'parkinglotmanager'
        db_table = 'cameralist'
        # permissions = [
        #     ('edit_cameralist', 'Can edit camera list')
        # ]


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class History(models.Model):
    parkingid = models.AutoField(primary_key=True)
    rfid = models.CharField(max_length=12, blank=True, null=True)
    parkinglotid = models.ForeignKey(
        'Parkinglotlist', models.DO_NOTHING, db_column='parkinglotid', blank=True, null=True)
    platenumber = models.CharField(max_length=15, blank=True, null=True)
    plateimgurl = models.CharField(max_length=255, blank=True, null=True)
    staffid = models.ForeignKey(
        'Stafflist', models.DO_NOTHING, db_column='staffid', blank=True, null=True)
    cameraid = models.ForeignKey(
        Cameralist, models.DO_NOTHING, db_column='cameraid', blank=True, null=True)
    inorout = models.BooleanField(blank=True, null=True)
    checktime = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'parkinglotmanager'
        db_table = 'history'


class Parking(models.Model):
    rfid = models.CharField(primary_key=True, max_length=12)
    parkinglotid = models.ForeignKey(
        'Parkinglotlist', models.DO_NOTHING, db_column='parkinglotid')
    platenumber = models.CharField(max_length=15, blank=True, null=True)
    plateimgurl = models.CharField(max_length=255, blank=True, null=True)
    checkintime = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'parkinglotmanager'
        db_table = 'parking'
        unique_together = (('rfid', 'parkinglotid'),)

    def __str__(self):
        return self.rfid


class Parkinglotlist(models.Model):
    parkinglotid = models.CharField(primary_key=True, max_length=6)
    parkinglotname = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        app_label = 'parkinglotmanager'
        db_table = 'parkinglotlist'

    def __str__(self):
        return self.parkinglotname


class Stafflist(models.Model):
    staffid = models.CharField(primary_key=True, max_length=6)
    stafffullname = models.CharField(max_length=30, blank=True, null=True)
    parkinglotid = models.ForeignKey(
        Parkinglotlist, models.DO_NOTHING, db_column='parkinglotid', blank=True, null=True)

    class Meta:
        app_label = 'parkinglotmanager'
        db_table = 'stafflist'