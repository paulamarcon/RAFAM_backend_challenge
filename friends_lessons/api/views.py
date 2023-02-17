from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from friends_lessons.models import User
from friends_lessons.api.serializers import UserSerializer

class UserApiView(APIView):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class UserFriendshipsApiView(APIView):
    def get(self, request):
        #Agarro todos los usuarios
        all_users = User.objects.all()

        all_registered_friendships = []

        #Itero sobre cada usuario
        for user in all_users:
            #Agarro los amigos del usuario
            all_friends_of_a_user = user.friends.all()

            #Solo si tiene amigos hago lo que sigue
            if len(all_friends_of_a_user) != 0:

                #Hago una lista con todos los nombres de todos los amigos del usuario
                all_friends_firstname = []
                for friend in all_friends_of_a_user:
                    all_friends_firstname.append(friend.firstname)

                all_registered_friendships.append( {
                "friend": user.firstname,
                "friendships": all_friends_firstname
                })

        return Response(status=status.HTTP_200_OK, data=all_registered_friendships)
