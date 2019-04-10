from django import forms
from .models import Post

class PostModelForm(forms.ModelForm): # 모델 폼 양식
    content = forms.CharField(
        label="content",
        widget = forms.Textarea(attrs={ # 여기 들어가는 게 속성값들
                'rows' : 5,
                'cols' : 50,
                'placeholder' : '지금 뭘 하고 계신가?',
            }))
        
    class Meta: # 디자인 부분
        model = Post # 어떤 모델에 대해서 만들지 먼저 말해주고
        # fields = '__all__' # 요로케 하면 그 모델에 대한 모든 필드에 대한 input이 만들어지지만 모두 가져올 필요가 별로 없음
        fields = ['content',]
