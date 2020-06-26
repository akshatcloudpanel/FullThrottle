from django.db import models



class ActivityPeriod(models.Model):
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()


class Member(models.Model):
    member_id = models.CharField(max_length=256,primary_key=True)
    real_name = models.CharField(max_length=256, blank=True)
    time_zone = models.CharField(max_length=256, blank=True)
    activity_periods = models.ManyToManyField("ActivityPeriod", blank=True, related_name="activity_periods")