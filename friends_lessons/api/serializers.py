from rest_framework.serializers import ModelSerializer
from friends_lessons.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['firstname', 'lastname']