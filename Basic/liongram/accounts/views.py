from django.shortcuts import render, redirect
from .forms import UserCreateForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django.contrib.auth import login

# Create your views here.

# 회원가입 View
def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)

    # POST 요청 시 데이터 확인 후 회원 생성
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            # 회원가입 처리
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password2 = form.cleaned_data['password2']
            instance = form.save()
            return redirect('index')
        else:
            # redirect로 돌리기
            return redirect('accounts:signup')




# 로그인 View
def login_view(request):
    # GET / POST 분리
    if request.method == 'GET':
        # 로그인 HTML 응답
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    else:
        # 데이터 유효성 검사
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache)
            # 응답 
            return redirect('index')
        else:
            # 비즈니스 로직 처리 - 로그인 실패 처리
            # 응답
            return render(request, 'accounts/login.html', {'form': form})


        # form을 사용하지 않을 경우
        # username = request.POST.get('username')
        # if username == '' or username == None:
        #     pass

        # user = User.objects.get(username=username)
        # if user == None:
        #     pass


    

