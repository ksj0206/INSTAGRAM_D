from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create(request):
    
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기
        form = PostModelForm(request.POST, request.FILES) # 모델폼으로 넘어온 데이터를 정리
        
        if form.is_valid(): # 유효성 검사
            post = form.save(commit=False) # save는 하고 db에 저장은 하지 마라
            post.user = request.user # 객체를 때려박아도 장고가 알아서 id 만 따와서 들어간다.
            post.save()
            return redirect('posts:list') # 일단은 리다렉
        
    
    # 아니고, GET 요청이 오면
    else: 
        # post를 작성하는 폼을 가져와 template에서 보여준다.
        form = PostModelForm()
        context = {
            'form':form
        }
        return render(request,'posts/create.html',context)

@login_required
def list(request):
    # 접속한 유저가 팔로잉한 유저들의 Post만 보여준다.
    # 동영 ver.
    # posts = []
    # for following in request.user.followings.all():
    #     posts.extend(Post.objects.filter(user=follwing))
    # 요거는 속도가 좀 안날 수도 있다.
    # 항상 데이터 찾는거는 DB에 시키자.
    # 쌤 ver.
    posts = Post.objects.filter(user__in=request.user.followings.values('id')).order_by('-pk')
    
    comment_form = CommentForm()
    context = {
        'posts':posts,
        'comment_form':comment_form,
    }
    return render(request,'posts/list.html',context)

@login_required
def delete(request, post_id):
    post = Post.get_object_or_404.get(Post,pk=post_id)
    
    if post.user != request.user:
        return redircet('posts:list')
    
    post.delete()
    return redirect('posts:list')

@login_required
def update(request, post_id):
    
    post = Post.get_object_or_404.get(Post,pk=post_id)
    
    if post.user != request.user:
        return redircet('posts:list')
        
    # POST 요청일 때
    if request.method == "POST":
        # 수정내용 DB에 반영
        form = PostModelForm(request.POST, instance=post) # 여기가 create 이랑 다른점
        if form.is_valid():
            form.save()
            return redirect('posts:list') # 디테일 아직 없으니까 일단 list
    
    # GET 요청일 때
    else:
        # 수정 내용 편집
        form = PostModelForm(instance=post) # 요로케 넘겨야 value 뜸
        context = {
            'form' : form,
        }
        return render(request, 'posts/update.html', context)

@login_required
def create_comments(request, post_id):
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # 일단 
        comment.user = request.user # 누가 작성했는지 넣어주고
        comment.post_id = post_id
        comment.save()
        return redirect('posts:list')
        
@login_required
def like(request,post_id):
    # 특정 유저가 특정 포스트를 좋아요 할 때
    post = get_object_or_404(Post,id=post_id) # 특정 유저는 request.user로 들어올 것.. 
    # 특정 포스트는 위처럼
    
    # 만약 좋아요가 되어 있다면,
    # -> 좋아요를 해제한다.
    if request.user in post.like_users.all(): # 만약 좋아요가 되어 있다면,
         post.like_users.remove(request.user)
     
    # 아니면
    # -> 좋아요를 한다.
    else:
        post.like_users.add(request.user) 
    
    return redirect('posts:list')