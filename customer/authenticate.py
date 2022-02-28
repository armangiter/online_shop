from .models import User


class PhoneBachEnd:
    def authenticate(self, request, phone=None):
        try:
            user = User.objects.get(phone=phone)
            if user:
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
