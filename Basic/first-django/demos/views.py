from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
import random                          # 로또 번호 추출 기능을 위해 random 모듈 import

# Create your views here.


# 계산기 기능 함수
def calculator(request):
    print(f'request = {request}')
    print(f'request type = {type(request)}')
    print(f'request.__dict__ = {request.__dict__}')

    # 1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':   
        result = int(num1) * int(num2) 
    elif operators == '/':   
        result = int(num1) / int(num2)     
    else:
        result = 0    


    # 3. 응답
    return render(request, 'calculator.html', {'result': result})



# 로또 번호 추출 기능 함수
def lotto(request):
    lotto_numbers = []        # lotto_numbers라는 리스트 생성
    numbers = range(1, 46)   # 1부터 45까지의 범위를 나타내는 변수 numbers 설정

    for number in numbers:   # 1~45에서 숫자 1개씩 뽑아서 lotto_numbers 리스트에 추가
        lotto_numbers.append(number)
    
    lotto_list = random.sample(lotto_numbers, 7)   # random 모듈 사용해서 lotto_numbers 리스트 중 무작위로 7개 뽑고 lotto_list에 저장

    context = {
        'lotto_list': lotto_list,
    }
        
    return render(request, 'lotto.html', context)
