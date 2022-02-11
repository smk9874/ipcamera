from django.db import models


class UserList(models.Model):

    mac_address = models.CharField(max_length=20)
    note = models.CharField(max_length=20)


class AlarmSetting(models.Model):

    motion_alarm = models.BooleanField(default=False)
    sound_alarm = models.BooleanField(default=False)
