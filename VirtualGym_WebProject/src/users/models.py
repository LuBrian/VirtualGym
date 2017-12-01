from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
# from oauth2client.contrib.django_orm import FlowField




"""/******************************
** File: models.py 
** Desc: This file forms the relevant back-end database structure for MyUsers in the VirtualGym web application.
** The tables are viewed as "models" in Django and are viewed as "tables" in the database.
*******************************/"""




class MyUsersManager(BaseUserManager):
	def _create_user(self, username,email, password, is_admin, is_superuser,**extra_fields):
		"""
		Creates and saves a User with the given email, and password.
		"""

		"""
		Override defualt user manager, create our own user manager for our
		custom model, performs create user actions

		@type  username: char
		@param username: the name of the user 
		@type  email: char
		@param email: The emails address that use used to sign up
		@type  password: char
		@param password: user account password
		@type  is_admin: boolean
		@param is_admin: if this is an admin or not
		@type  is_superuser: boolean
		@param is_superuser: if this ueser an superuser or not
		"""

		print("get create user")
		print(email)
		print(password)
		now = timezone.now()
		# if MyUsers._default_manager.get(email=email) != None:
		# 	print("user already exists by email")
		# 	raise ValueError('Email is already used, please use a new email.')

		# if user social sign in and email exist, assign email attribute
		if(email):
			print("has email")
			user = self.model(
				email=email,
				last_login = now,
				date_joined=now,
				username = username,
				is_active = True,
				is_admin = is_admin,
				is_superuser = is_superuser,
			)
		else:
			# else auto assign an email address to this social account
			print("no email")
			user = self.model(
				email=username+"@vg.ca",
				last_login = now,
				date_joined=now,
				username = username,
				is_active = True,
				is_admin = is_admin,
				is_superuser = is_superuser,
			)
		if password != None:
			user.password = password

		user.save(using=self._db)
		return user
	# used when user sign up on web page
	def create_user(self,username, email, password = None,**extra_fields):
		print("creat normal user")
		return self._create_user(username,email,password,False, False, **extra_fields)
	# used by admin by typing createsuperuser in console
	def create_superuser(self, username,email, password, **extra_fields):

	    return self._create_user(username,email,password ,True, True, **extra_fields)

class MyUsers(AbstractBaseUser):
	"""
	Extended from defual user model, customize own "MyUsers" model to have more
	flexibility

	@type  username: char
	@param username: the name of the user 
	@type  email: char
	@param email: The emails address that use used to sign up
	@type  password: char
	@param password: user account unique id
	@type  user_id: char
	@param user_id: user account unique id
	@type  password: char
	@param password: user account password
	@type  is_active: Boolean
	@param is_active: user account active or not
	@type  is_admin: boolean
	@param is_admin: if this is an admin or not
	@type  is_superuser: boolean
	@param is_superuser: if this ueser an superuser or not
	@type  last_login: date 
	@param last_login: when is the user last time logged in
	@type  date_joined: date
	@param date_joined: when the user first time use the app 
	"""
	email = models.EmailField(blank = True,null=False,unique=True)
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(blank = True,max_length=50,unique=True)
	password = models.CharField(blank = True,max_length=50)
	last_login = models.DateTimeField(_('date joined'), default=timezone.now,null=True)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now,null=True)

	is_active    = models.BooleanField(default=True)
	is_admin     = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [ 'username']
	print("create a user")
	objects = MyUsersManager()
	class Meta:
		verbose_name = ('user')
		verbose_name_plural = ('users')

	# return the user name of MyUser is string(MyUser)
	def __str__ (self):
		return str(self.username)

	# return true or false to indicate if the user is superuser or not
	def has_perm(self, perm, obj=None):
		return self.is_superuser

	# check this MyUser object's password with the input password 
	# and return true if input passwor correct, else false
	def check_password(self,password):
		return self.password == password

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser

	# return the MyUser object's full name, now just return the email
	# will be further modified if needed
	def get_full_name(self):
	# The user is identified by their email address
		return self.email

	# return the MyUser object's short name, now just return the email
	# will be further modified if needed
	def get_short_name(self):
	# The user is identified by their email address
		return self.email

	# return the MyUser's id
	def get_user_id(self):
		return self.user_id

	# return if the user is super user or not
	def check_superuser(self):
		return self.is_superuser

	# set the password for this user
	def set_a_password(password):
		self.password = password

	def __str__(self):              # __unicode__ on Python 2
		return self.email

	@property
	def is_staff(self):
	# "Is the user a member of staff?"
	# Simplest possible answer: All admins are staff
		return self.is_admin
