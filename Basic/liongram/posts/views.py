from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# 클래스 뷰를 위한 상속
from django.views.generic.list import ListView
from .models import Post

# Create your views here.


# index 페이지 연결하기
def index(request):
    return render(request, 'index.html')


# CRUD template 연결하기
def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')

def post_create_view(request):
    return render(request, 'posts/post_form.html')

def post_update_view(request, id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')




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