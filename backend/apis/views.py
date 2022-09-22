from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken, Token
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .customPermission import isAdmin
from .models import Book, CustomUser
from .serializers import BookSerializer, CreateUserSerializer,ChangeUserSerializer


class BookAdminViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # using custom permision class and onl allowing users with usertype = 1 
    permission_classes = [isAdmin]
    # using token based authenctication system. 
    authentication_classes = [TokenAuthentication]

class BookStudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [isAdmin]
    # using token based authenctication system. 
    authentication_classes = [TokenAuthentication]

    def partial_update(self,request , *args,**kwargs):

        user_obj = self.get_object()
        data = request.data
        user_obj.UserType = str(data['UserType'][0])
        user_obj.first_name = data['first_name']
        user_obj.save()
        serializer = CreateUserSerializer(user_obj)
        return Response(serializer.data)

    
    # creating custom token obtaining class as simple class only return token for a user 
    # after successsful login ,
    #  while i wanted its userid as well as it usertype with it
class Custom_auth_token(ObtainAuthToken):
    def post(self , req , *args , **kwargs):
        serializer = self.serializer_class(data = req.data , context = {'request' : req})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token , created = Token.objects.get_or_create(user = user)
        return Response({"token" : token.key,
        'user_id' : user.pk , 
        'UserType' : user.UserType} , status=status.HTTP_200_OK)




