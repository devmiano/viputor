from api.serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view


User = get_user_model()


@api_view(['GET'])
def get_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_patron(request):
    try:
        data = request.data
        city = data['city']
        address = data['address']
        location = data['location']
        user_id = data['user_id']
        user = User.objects.get(id=user_id)
    except:
        return Response({'error': 'The user_id provided doesnot exist. Try again'}, status=status.HTTP_404_NOT_FOUND)

    user.city = city
    user.address = address
    user.location = location
    user.is_patron = True
    user.save()

    serializer = UserSerializer(user)

    return Response(serializer.data)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'
