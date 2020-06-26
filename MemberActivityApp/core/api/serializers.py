from rest_framework import serializers
from django.apps import apps
Member = apps.get_model('core', 'Member')
ActivityPeriod = apps.get_model('core','ActivityPeriod')


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField(method_name='get_start_time')
    end_time = serializers.SerializerMethodField(method_name='get_end_time')

    class Meta:
        fields = ('start_time','end_time')
        model = ActivityPeriod

    def get_start_time(self,obj):
        return obj.start_time.strftime("%b %d %Y, %-I:%M%p")

    def get_end_time(self,obj):
        return obj.end_time.strftime("%b %d %Y, %-I:%M%p")



class MembersSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(read_only=True, many=True)

    class Meta:
        fields = ['member_id', 'real_name', 'time_zone', 'activity_periods']
        model = Member

