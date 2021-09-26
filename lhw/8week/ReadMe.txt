1번문제. baseball game

- 1세트당 총 **10번**의 기회가 주어집니다.
- 사용되는 숫자는 **1에서 9까지** 서로 다른 숫자입니다. **중복을 허용하지 않습니다**.
- 숫자는 맞지만 위치가 틀렸을 때는 **볼**입니다.

    ex) 입력/정답: 4,2,**8** / 3,**8**,9 → 숫자8은 정답에 존재하지만 위치 다름

- 숫자와 위치가 전부 맞으면 **스트라이크**입니다.

    ex) 입력/정답: **4**,2,8 / **4**,1,9 → 숫자4는 정답에 존재하고 위치까지 동일

- **3 스트라이크**시 게임 종료

(베이스라인)
```python
import random
import datetime

def checkBallStrike(x, answer):
		##################
		# 여기를 채우세요 #
		##################
    return ball,strike

def game_one_round():  
		###############################################
		# 여기를 채우세요                              #
		# 리턴값: 계속 게임할 경우 True 아닐경우 False  #
		###############################################
		# ball,strike = checkBallStrike(x, answer) # 이 함수를 활용하세요
    return True

def main():
		#############################
		# main 함수는 건들면 안됩니다 #
		#############################
    print('-'*50)
    print(f'[{str(datetime.datetime.now())[:-7]}] 숫자 야구 게임을 시작합니다!')
    bContinue = True
    while bContinue:
        count, score, answer = 0,10,(0,0,0)
        bContinue = game_one_round()

    print('-'*50)
    print(f'[{str(datetime.datetime.now())[:-7]}] 숫자 야구 게임을 종료합니다!')
```

2번문제

- M 증권사에서는 고객 거래 내역 데이터를 이용해 VIP 고객 명단을 추출하고 이를 text 파일로 저장하려 합니다.
- "customer_data" 딕셔너리는 고객의 이름을 키(key)값으로 하고 해당 고객이 지금까지 지출한 수수료를 벨류(value) 값으로 갖습니다.
- 현재 코드를 작성 중인 디렉토리 안에서 **"customer"이라는 하위 디렉토리가 없을 경우 "customer" 디렉토리를 새로 만들고**, 해당 디렉토리 안에 **지출 수수료가 10,000 이상인 고객들의 이름과 지출 수수료가 한줄씩 정리된 text 파일을 "vip_list.txt"라는 이름으로 생성해 주세요.**
