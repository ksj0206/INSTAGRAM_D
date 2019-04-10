from django.shortcuts import render, redirect
from .forms import PostModelForm

# Create your views here.
def create(request):
    
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기
        form = PostModelForm(request.POST) # 모델폼으로 넘어온 데이터를 정리
        
        if form.is_valid(): # 유효성 검사
            form.save() # 통과되면 저장
            return redirect('posts:create') # 일단은 리다렉
        
    
    # 아니고, GET 요청이 오면
    else: 
        # post를 작성하는 폼을 가져와 template에서 보여준다.
        form = PostModelForm()
        context = {
            'form':form
        }
        return render(request,'posts/create.html',context)