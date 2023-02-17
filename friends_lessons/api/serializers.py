from rest_framework.serializers import ModelSerializer
from friends_lessons.models import User, Lesson

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['firstname', 'lastname']

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name']