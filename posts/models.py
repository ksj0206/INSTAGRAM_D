from django.db import models
from django.conf import settings 

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True)
    # User와의 연결고리를 만들어줘야 함.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 실제 DB에는 user객체가 들어가는 게 아니라 user_id 만 만들어져서 들어감
    # ForeignKey(Modelclass, Options)
    # User를 import 해서 안쓰는 이유는 장고가 이미 포장해서 다른 말로 만들어놨으니까 그거 쓰려구
    
    
    def __str__(self):
        return f"{self.id} : {self.content[:20]}"
        
    def __repr__(self):
        return f"{self.id} : {self.content[:20]}"