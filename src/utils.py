import random
'''
game_clear 조건 <guess == target_num> 
game_over 조건 < 컨트롤+C 누르면 종료>
'''

def select_difficulty():
    easy = random.randint(1,10)
    medium = random.randint(1,50)
    hard = random.randint(1,100)

    difficulty = {'1':easy,'2':medium,'3':hard}
    select_difficulty = str(input("난이도를 선택해주세요.  1 : 쉬움\n2 : 중간\n3 : 어려움"))

    return difficulty[select_difficulty]

