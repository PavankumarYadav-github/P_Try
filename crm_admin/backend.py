# backends.py

from crm_admin.models import User
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ValidationError

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        print(email,password)
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                print(f"User authenticated: {user}")
                return user
            else:
                raise ValidationError("Password does not match.")
        except User.DoesNotExist:

            raise ValidationError("User with this email does not exist.")
