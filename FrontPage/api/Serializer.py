from FrontPage.models import User_Activity
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model= User_Activity
        Fields=[
            'id',
            'FullName',
            'location',
            'start_time',
            'End_time'
        ]
