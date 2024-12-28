# account/backends.py

# 📦 Import necessary modules
import logging
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

# Get the User model
User = get_user_model()

# Configure logging
logger = logging.getLogger(__name__)

# Define a custom authentication backend
class AuthenticationBackend(ModelBackend):
    # Override the authenticate method
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if username is either email or username
            user = User.objects.filter(username__iexact=username).first()
            if not user:
                user = User.objects.filter(email__iexact=username).first()
            # Check if the user exists and the password is correct
            if user and user.check_password(password) and self.user_can_authenticate(user):
                return user
        except Exception as e:
            # Log the exception
            logger.error("An error occurred during authentication: %s", e)
        return None
