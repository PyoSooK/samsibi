import random


'''
game_clear 조건 <guess == target_num> 
game_over 조건 < 컨트롤+C 누르면 종료>
'''

def start():
    target_num = random.randint(0,10)
    while True:
        cnt=0
        user_input = int(input("값을 입력해주세요.: "))

        if user_input  == target_num :
            print("정답입니다. ! 게임을 다시 시작할까요? Y/N 을 입력해주세요.")
            while True:
                command = input()
                command = command.lower()

                if command =='y':
                    target_num = random.randint(0,10)
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














