from django.db import models


class User(models.Model):

    mac_address = models.CharField(max_length=20)
    note = models.CharField(max_length=20, default='', editable=True)

    def __str__(self):

        return self.mac_address


class AlarmSetting(models.Model):

    motion_alarm = models.BooleanField(default=False)
    sound_alarm = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_uniq_id', default=1)

