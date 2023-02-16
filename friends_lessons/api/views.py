from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from friends_lessons.models import User
from friends_lessons.api.serializers import UserSerializer

class UserApiView(APIView):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
