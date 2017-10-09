from models import MyUsers


# class MyUsersAuth(object):

# 	def authenticate(self, email = None, password = None):

# 		try:
# 			user = MyUsers.objects.get(email=email)
# 			if user.check_password(password):
# 				return user
# 		except MyUsers.DoesNotExist:
# 			return None


# 	def get_user(self, id):

# 		try:
# 			user= MyUsers.objects.get(pk=id)
# 			if user.is_active:
# 				return user
# 			return None
# 		except MyUsers.DoesNotExist:
# 			return None