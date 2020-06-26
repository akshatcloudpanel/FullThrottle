from django.urls import path
from .views import *



urlpatterns = [

    path('memberList/', MembersList.as_view(), name="member_list"),

]