from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")
    # 여기가 포인트 다른 놈이 나를 부를 때 follwers가 아니라 following이니까 realted_name 요로케 줘야함
    
    