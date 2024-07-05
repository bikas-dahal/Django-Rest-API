from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.models import User

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            return None
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('No such user')
        
        return (user, None)
        
        # token = request.META.get('HTTP_AUTHORIZATION')
        # if not token:
        #     return None
        # try:
        #     token = Token.objects.get(key=token)
        # except Token.DoesNotExist:
        #     return None
        # return token.user, token