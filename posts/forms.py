from django import forms
from .models import Post

class PostModelForm(forms.ModelForm): # 모델 폼 양식
    content = forms.CharField(label="content")
    
    class Meta:
        model = Post # 어떤 모델에 대해서 만들지 먼저 말해주고
        # fields = '__all__' # 요로케 하면 그 모델에 대한 모든 필드에 대한 input이 만들어지지만 모두 가져올 필요가 별로 없음
        fields = ['content',]