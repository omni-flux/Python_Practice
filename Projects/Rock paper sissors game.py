import random
import sys

print("Welcome to rock,paper,scissor..")

moves : dict = {'rock':'🪨','paper':'📄','scissors':'✂️'}
valid_moves:list[str] = list(moves.keys())
human_score:int = 0
ai_score:int = 0

while True:
    user_input:str = input("rock,papers or scissors >>>").lower()
    if user_input == 'exit':
        print('-----------------------------------')
        print('thanks for playing....')
        print(f"scores:\n"
              f"🧑: {human_score}\n"
              f"🤖: {ai_score}")
        print('-----------------------------------')

        sys.exit()
    if user_input not in valid_moves:
        print('Please Enter a valid move')
        continue
    ai_move : str = random.choice(valid_moves)

    print('-----------------------------------')
    print(f"you:{moves[user_input]}")
    print(f"ai:{moves[ai_move]}")
    print('-----------------------------------')

    if user_input == ai_move:
        print("it's a draw")
    elif user_input == "rock" and ai_move == "scissors":
        print("you win!")
        human_score+=1
    elif user_input == "scissors" and ai_move == "paper":
        human_score += 1
        print("you win!")
    elif user_input == "paper" and ai_move == "rock":
        human_score += 1
        print("you win!")
    else:
        print('you loose...')
        ai_score += 1



