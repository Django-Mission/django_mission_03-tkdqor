from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
# 클래스 뷰를 위한 상속
from django.views.generic.list import ListView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.http import Http404     # Http404를 import
from .forms import PostBaseForm, PostCreateForm, PostDetailForm

# Create your views here.


# index 페이지 연결하기
def index(request):
    post_list = Post.objects.all().order_by('-created_at')   # Post 전체 데이터 조회
    context = {
        'post_list': post_list,
    }

    return render(request, 'index.html', context)


# CRUD template 연결하기

def post_list_view(request):
    # post_list = Post.objects.all()   # Post 전체 데이터 조회
    post_list = Post.objects.filter(writer=request.user)    # Post.writer가 현재 로그인된 경우 조회
    context = {
        'post_list': post_list,
    }

    return render(request, 'posts/post_list.html', context)


def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)        # 게시글 1개에 대한 데이터 가져오기
    except Post.DoesNotExist:
        return redirect('index')

    context = {
        'post': post,
        'form': PostDetailForm(),
    }

    return render(request, 'posts/post_detail.html', context)


@login_required                  # 로그인 되었을 경우에만 가능하게 하기
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')             # 이미지 파일을 받을 경우, request.FILES로 사용
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(image=image, content=content, writer=request.user) # writer=request.user 추가 필요
        return redirect('index')



# forms.py를 이용해서 View 설정
def post_create_form_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {
            'form': form,
        }
        return render(request, 'posts/post_form2.html', context)
    else:
        form = PostCreateForm(request.POST, request.FILES)

        # form 자체에 대한 유효성 검사
        if form.is_valid():
            Post.objects.create(image=form.cleaned_data['image'], content=form.cleaned_data['content'], writer=request.user) 
        else:
            return redirect('posts:post-create')
        
        return redirect('index')



@login_required                  # 로그인 되었을 경우에만 가능하게 하기
def post_update_view(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id, writer=request.user)

    if request.method == 'GET':
        context = { 'post': post, }
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        print(new_image)
        print(content)

        if new_image:
            post.image.delete()     # 기존의 이미지를 먼저 삭제
            post.image = new_image  # 그리고 새로운 이미지로 교체

        
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)


@login_required                  # 로그인 되었을 경우에만 가능하게 하기
def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.writer:
        raise Http404('잘못된 접근입니다.')

    if request.method == 'GET':
        context = {
        'post': post,
        }
        return render(request, 'posts/post_confirm_delete.html', context)
    else:
        post.delete()
        return redirect('index')

    
    






# HttpResponse 또는 JsonResponse 사용해보기
def url_view(request):
    print('url_view()')
    data = {'code': '001', 'msg': 'OK'}
    # return HttpResponse('<h1>url_view</h1>')
    return JsonResponse(data)


# url 변수 데이터 받아보기
def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)


# Http method GET 또는 POST따라 데이터 받기
def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')


# Class View(ListView) 사용해보기
class class_view(ListView):
    model = Post
    ordering = ['-id']
    template_name = 'cbv_view.html'