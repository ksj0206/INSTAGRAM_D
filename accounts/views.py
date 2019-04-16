from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login as auth_login # 이러케 하는 이유는 밑에 정의할 login 함수랑 겹쳐서 라이브러리 설명은 공식문서 찾아주셈
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    # 회원가입
    if request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid(): # 야 폼아 혹시 넘어온 데이터 괜찮닝
            user = form.save() # 방금 가입한 유저
            auth_login(request,user)
        return redirect('posts:list')
    else:
        form = UserCreationForm()
        context = {
            'form':form,
        }
        return render(request, 'accounts/signup.html',context)
        
def logout(request):
    auth_logout(request)
    return redirect('posts:list')

def login(request):
    if request.method == "POST":
        # 실제 로그인 (세션에 유저 정보를 넣는다.)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) # form.get_user 는 form 으로 부터 유저 정보를 가져오는 함수
        return redirect('posts:list')
            
    else:
        # 유저로부터 username과 비밀번호를 받는다.
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'accounts/login.html',context)