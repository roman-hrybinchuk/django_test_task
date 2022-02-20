from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from shop_managment.models import Worker


class CustomAuth(BaseAuthentication):
    def authenticate(self, request):

        phone = request.META.get('HTTP_AUTHORIZATION')
        if not phone:
            return None

        try:
            user = Worker.objects.get(phone_number=phone)
        except Worker.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
