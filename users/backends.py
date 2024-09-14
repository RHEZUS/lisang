from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from .models import CustomUser  # Adjust the path if necessary

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Use the custom user model
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

