import random
import datetime

def checkBallStrike(x, answer):
    ball,strike = (0,0)
    for y_pred,y_true in zip(x,answer):
        if y_pred in answer and y_pred == y_true:
            strike = strike + 1
        else:
            if y_pred in answer:
                ball = ball + 1
    return ball,strike

def game_one_round():
    print('-'*50)
    print(f'[{str(datetime.datetime.now())[:-7]}] 서로 다른 3개의 숫자를 입력해주세요! ex) 3,6,9')

    ###############
    # 게임 초기화 #
    ###############
    answer = random.sample(range(1, 10), 3)  # 정답 생성
    count = 1

    while True:
        ##################
        # 남은 횟수 체크 #
        ##################
        if count >= 10:
            break

        ##################
        # 남은 횟수 출력 #
        ##################
        print('-'*50)
        print(f'[{str(datetime.datetime.now())[:-7]}] 남은 횟수: {10-count}')

        #################
        # 사용자의 입력 #
        #################
        print('-'*50)
        x = list(map(lambda x:int(x),input(f'[{str(datetime.datetime.now())[:-7]}] 입력: ').strip().split(',')))

        #############################
        # 서로 다른 숫자들인지 체크 #
        #############################
        if len(set(x)) != 3:
            print(f'[{str(datetime.datetime.now())[:-7]}] 서로 다른 3개의 숫자를 입력해주세요!')
            continue

        #######################
        # 볼, 스트라이크 계산 #
        #######################
        ball,strike = checkBallStrike(x, answer)

        #######################
        # 게임 종료 조건 체크 #
        #######################
        if strike == 3:
            print('-'*50)
            score = 10 - count
            print(f'[{str(datetime.datetime.now())[:-7]}] 축하합니다! 당신의 점수는 {score}점입니다!')
            break
        print('-'*50)
        print(f'[{str(datetime.datetime.now())[:-7]}] {strike}스트라이크 {ball}볼')
        count = count + 1

    ####################
    # 사용자 점수 계산 #
    ####################
    print('-'*50)
    print(f'[{str(datetime.datetime.now())[:-7]}] 수고하셨습니다. 정답은 {answer}입니다!')

    print('-'*50)
    more = input(f'[{str(datetime.datetime.now())[:-7]}] 게임을 다시 할까요? [Y/N]: ').lower()

    if more == 'n':
        return False
    return True

def main():
    print('-'*50)
    print(f'[{str(datetime.datetime.now())[:-7]}] 숫자 야구 게임을 시작합니다!')
    bContinue = True
    while bContinue:
        count, score, answer = 0,10,(0,0,0)
        bContinue = game_one_round()

    print('-'*50)
    print(f'[{str(datetime.datetime.now())[:-7]}] 숫자 야구 게임을 종료합니다!')
```
