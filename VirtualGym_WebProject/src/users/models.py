from django.db import models

# Create your models here.
class SignUp(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50,null=False)
    user_password = models.CharField(max_length=50,null=False)
    #timestamp=models.DataTimeField(auto_now_add=True,auto_now=False)
    def __str__ (self):
        return "%s %s" %(self.user_id,self.user_name)
