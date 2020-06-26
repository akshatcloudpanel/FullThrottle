from django.core.management.base import BaseCommand
# from django.utils import timezone
# import os
import django
django.setup()
from random import *
from faker import Faker
fake = Faker()
from django.apps import apps
Member = apps.get_model('core', 'Member')
ActivityPeriod = apps.get_model('core','ActivityPeriod')


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for i in range(5):
            members_records = Member.objects.create(member_id=fake.pystr(), real_name=fake.name(), time_zone=fake.timezone())

            for j in range(0, randint(0, 4)):
                members_records.activity_periods.add(
                    ActivityPeriod.objects.create(start_time=fake.date_time(), end_time=fake.date_time()))

