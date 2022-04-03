from multiprocessing import context
from django.shortcuts import render
import random                          # 로또 번호 추출 기능을 위해 random 모듈 import

# Create your views here.

# 로또 게임 수 입력 페이지
def lotto(request):

    return render(request, 'lotto.html')



# 로또 번호 추출기 결과 페이지 
def result(request):

    # count라는 이름의 GET방식 데이터를 받아서 game_count 변수에 저장 + int()를 사용해서 정수로 변경
    game_count = int(request.GET.get('count'))

    lotto_numbers = []       # lotto_numbers라는 리스트 생성
    numbers = range(1, 46)   # 1부터 45까지의 범위를 나타내는 변수 numbers 설정

    for number in numbers:   # 1~45에서 숫자 1개씩 뽑아서 lotto_numbers 리스트에 추가
        lotto_numbers.append(number)

    lotto_lists = random.sample(lotto_numbers, 7)  # random 모듈 사용해서 lotto_numbers 리스트 중 무작위로 7개 뽑고 lotto_list에 저장

    # 입력받은 게임 개수를 range함수로 범위 설정
    counts = range(game_count)


    context = {
        'game_count': game_count,
        'lotto_lists': lotto_lists,
        'counts': counts,
    }

    return render(request, 'result.html', context)