from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
# from oauth2client.contrib.django_orm import FlowField


class MyUsersManager(BaseUserManager):
	def _create_user(self, email, password, is_admin, is_superuser,**extra_fields):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""

		# if not email:
		#     raise ValueError('Users must have an email address')
		# email=self.normalize_email(email)
		print("get create user")
		print(email)
		print(password)
		now = timezone.now()
		user = self.model(
			email=email,
			last_login = now,
			date_joined=now,
			username = email,
			is_active = True,
			is_admin = is_admin,
			is_superuser = is_superuser,
		)
		if password != None:
			user.password = password

		user.save(using=self._db)
		return user

	def create_user(self, email, password = None,**extra_fields):
		print("creat normal user")
		return self._create_user(email,password,False, False, **extra_fields)
	def create_superuser(self, email, password, **extra_fields):

	    return self._create_user(email,password ,True, True, **extra_fields)
	    # Create your models here.

class MyUsers(AbstractBaseUser):
	email = models.EmailField(blank = True,null=False)
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(blank = True,max_length=50,unique=True)
	password = models.CharField(blank = True,max_length=50)
	last_login = models.DateTimeField(_('date joined'), default=timezone.now,null=True)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now,null=True)

	is_active    = models.BooleanField(default=True)
	is_admin     = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = [ 'email']
	print("create a user")
	objects = MyUsersManager()
	class Meta:
		verbose_name = ('user')
		verbose_name_plural = ('users')

	def __str__ (self):
		return str(self.username)

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser

	def check_password(self,password):
		return self.password == password

	def get_full_name(self):
	# The user is identified by their email address
		return self.email

	def get_short_name(self):
	# The user is identified by their email address
		return self.email

	def get_user_id(self):
		return self.user_id


	def check_superuser(self):
		return self.is_superuser


	def set_a_password(password):
		self.password = password

	def __str__(self):              # __unicode__ on Python 2
		return self.email

	# def has_perm(self, perm, obj=None):
	# "Does the user have a specific permission?"
	# # Simplest possible answer: Yes, always
	# 	return True

	# def has_module_perms(self, app_label):
	# "Does the user have permissions to view the app `app_label`?"
	# # Simplest possible answer: Yes, always
	# 	return True

	@property
	def is_staff(self):
	# "Is the user a member of staff?"
	# Simplest possible answer: All admins are staff
		return self.is_admin
