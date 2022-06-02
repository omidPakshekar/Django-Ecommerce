from django.db import models
# from django.contrib.auth.models import AbstractBaseuser, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.username + ".png"}'

def get_default_profile_image():
    return "customers/default_profile_image.png"

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save()
		return user


class CustomUser(AbstractBaseUser):
    class Meta:
        verbose_name_plural = "Customers"

    email 				= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username 			= models.CharField(max_length=30, unique=True)
    date_joined			= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login			= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin			= models.BooleanField(default=False)
    is_active			= models.BooleanField(default=True)
    is_staff			= models.BooleanField(default=False)
    is_superuser		= models.BooleanField(default=False)
    profile_image       = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    hide_email          = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f"profile_images/{self.pk}"):]
	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
    	return True


class DiscountCode(models.Model):
    class Meta:
        verbose_name_plural = "DiscountCode"

    user               = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    code               = models.CharField(max_length=12, unique=True)
    started_time       = models.DateTimeField()
    expired_time       = models.DateTimeField()
    percent            = models.PositiveIntegerField()

    def __str__(self):
        return str(self.percent) + "%"


class Address(models.Model):
    class Meta:
        verbose_name_plural = "Adresses"

    user               = models.ForeignKey(CustomUser, blank=False, null=False, on_delete=models.CASCADE)
    firstname          =  models.CharField(max_length=30, blank=False, null=False)
    lastname           = models.CharField(max_length=30, blank=False, null=False)
    address_text       = models.CharField(max_length=1200, blank=False, null=False)
    country            = models.CharField(max_length=40, default='ایران', null=False)
    province           = models.CharField(max_length=100, blank=False, null=False)
    city               = models.CharField(max_length=100, blank=False, null=False)
    postcode           = models.CharField(max_length=12, blank=False, null=False)
    phone_number       = models.CharField(max_length=11, blank=False, null=False)

    def __str__(self):
        return f"{self.province}_{self.city}_{self.address_text}"
