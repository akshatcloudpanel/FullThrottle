# FullThrottle
MemberActivityApp Project
--------------------


Note : First of all, create a Virtual Environment and install requirements.txt.

Models
------------

Theere are two models in the project - 

1. Member
2. ActivityPeriod

The Member model is linked to the ActivityPeriod by many-to-many field.



The Custom Command
-------------------

For the custom command , a file named 'populate_dummy_member.py' is kept at path '/MemberActivityApp/core/management/commands'.

The file has a command class in which the handle method defines an operation which the custom command will perform,
i.e. populating the database with dummy Member data.

The command works like this - 

'python3 manage.py populate_dummy_member'



The API
---------

The only api required is the memberList api which will display the data in the format as shown in the sample json.

A class based view is written , which on a GET request, uses a MemberSerializer to display the Member data.

The serializer is supplied with SerializerMethodField() to return the datetime data in desired format.

The url path for this api is 'home:port/api/memberList/'
