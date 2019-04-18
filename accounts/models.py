from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")
    # 여기가 포인트 다른 놈이 나를 부를 때 follwers가 아니라 following이니까 realted_name 요로케 줘야함
    
class Profile(models.Model):
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) # 1:1 일 때는 이 Field를 사용 / 모델에서는 settings.AUTH_USER_MODEL 쓰기로 했다.
    image = models.ImageField()
    
    
    def __str__(self):
        return f"{self.user.username}의 프로필"