from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login as auth_login # 이러케 하는 이유는 밑에 정의할 login 함수랑 겹쳐서 라이브러리 설명은 공식문서 찾아주셈
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    # 회원가입
    if request.method == "POST": 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 야 폼아 혹시 넘어온 데이터 괜찮닝
            user = form.save() # 방금 가입한 유저
            auth_login(request,user)
        return redirect('posts:list')
    else:
        form = CustomUserCreationForm()
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

@login_required       
def profile(request, username):
    # username을 가진 유저의 상세 정보를 보여주는 페이지
    profile = get_object_or_404(get_user_model(), username=username)
    context = {
        'profile':profile
    }
    return render(request,'accounts/profile.html',context)

@login_required    
def delete(request):
    # POST -> 계정을 삭제한다. == DB에서 user를 삭제한다.
    if request.method == "POST":
        request.user.delete()
        return redirect('accounts:signup')
    # GET -> 진짜 삭제하시겠습니까?
    return render(request,'accounts/delete.html')

@login_required
def follow(request, user_id): # 내가 팔로우 할 사람이 넘어 온다.
    person = get_object_or_404(get_user_model(), pk=user_id) # 내가 팔로우 하려는 사람을 일단 찾아.
    # 만약 이미 팔로우한 사람이라면,
    if request.user in person.followers.all(): # 내가(로그인한 사용자) 펄슨의 팔로우 들에 이미 있다면
        # 언팔
        person.followers.remove(request.user)
    # 아직 안했다면
    else:
        # 팔
        person.followers.add(request.user)
    return redirect('profile',person.username)
    
    