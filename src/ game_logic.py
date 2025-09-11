import random

def main_game_logic(max_number, guess, count):
    correct_number = random.randint(0, max_number)
    if correct_number == guess:
        answer = "정답"
        return count, answer
    elif correct_number > guess:
        answer = "업"
    else:
        answer = "다운"
    count += 1
    return answer, count