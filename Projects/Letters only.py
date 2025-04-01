import string
import sys

def is_letter(text:str)-> None:
    alphabet:str = string.ascii_letters + ' '

    for char in text:
        if char not in alphabet:
            raise ValueError("enter a valid str")
    print(f'{text} only has characters from the english alphabet 😊')


def main() -> None:
    print('-'*20+'welcome to letter only'+'-'*20)
    while True:
        try:
            user_input:str = input('enter a str:')
            is_letter(user_input)
        except KeyboardInterrupt:
            sys.exit()
        except ValueError:
            print(f'please enter a valid value')
        except Exception as e:
            print(f'the program encountered an error:{e} of type:{type(e)}')
        if user_input in ['exit','quit','q','bye-bye']:
            print('bye-bye 👋')
            sys.exit()

main()