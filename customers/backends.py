from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

 #  case insensetive model for user model
# if you write your email with capital it won't be a mistake

# if you use this class is does not matter if the username are captial or not

class CaseInSensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        userModel = get_user_model()
        if username is None:
            username = kwargs.get(userModel.USERNAME_FIELD)
        try:
            case_insensitive_username_field = "{}__iexact".format(userModel.USERNAME_FIELD)
            user = userModel._default_manager.get(**{case_insensitive_username_field: username})
        except userModel.DoesNotExist:
            # if does not exist create new one
            userModel().set_password(password)
        else :
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
