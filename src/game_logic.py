import random
from utils import select_difficulty



def start():
    cnt=0
    target_num = select_difficulty()
    while True:
        user_input = int(input("값을 입력해주세요.: "))

    
        if user_input  == target_num :
            print("정답입니다. ! 게임을 다시 시작할까요? Y/N 을 입력해주세요.")
            while True:
                command = input()
                command = command.lower()

                if command =='y':

                    start()
                    continue

                elif command =='n':
                    print("게임을 종료합니다.")
                    exit()

                else:
                    print("다시 입력해주세요.")

        else:

            if target_num > user_input:
                print('UP!')

            elif target_num<user_input:
                print('Down!')

        
        cnt+=1

try:
    start()

except KeyboardInterrupt:
    print("\n사용자에 의해 종료되었습니다.")














