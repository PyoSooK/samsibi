
def set_difficulty(level):
    # 난이도 설정 
    # 쉬움(1~100): 1, 보통(1~500): 2, 어려움(1~1000): 3
    if level == 1:
        return (1, 100)
    elif level == 2:
        return (1, 500)
    elif level == 3:
        return (1, 1000)
    else:
        raise ValueError("Invalid difficulty level. Choose 1, 2, or 3.")
