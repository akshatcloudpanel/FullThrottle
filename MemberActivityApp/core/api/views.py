from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps
Member = apps.get_model('core', 'Member')
ActivityPeriod = apps.get_model('core','ActivityPeriod')


class MembersList(APIView):
    """
    List all members with Activity periods
    """
    def get(self,request):
        members = Member.objects.all()
        serializer = MembersSerializer(members, many=True)
        response = {
            'ok':True,
            'members':serializer.data
        }
        return Response(response)