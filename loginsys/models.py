from django.db import models
from django.contrib.auth.models import User



class UserC(User):
   
        

        phone = models.IntegerField(default= 0 , verbose_name='Номер телефона')
        avatar = models.ImageField(upload_to= 'avatars', blank=True, null=True, verbose_name='Аватар')