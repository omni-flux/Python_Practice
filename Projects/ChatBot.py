from datetime import datetime
import sys

def get_response(text:str,name:str) -> str:
    lowered = text.lower()

    if lowered in ['hello','hi','ola','cho','ni hao']:
        return f'hello how are you! {name}😊'
    elif lowered in ['how are you','how are you doing']:
        return f"i'm doing great 👍, how are you doing {name}?"
    elif 'time' in lowered:
        current_time : datetime = datetime.now()
        return f"the current time is {current_time:%H:%M}"
    elif 'name' in lowered:
        return 'watashi no nawa kira yoshikage! '
    elif 'marco' in lowered:
        return 'polo'
    elif lowered in ['bye','see you','bye bye','good bye']:
        return 'it was nice talking to you thank you'
    elif 'joke' in lowered:
        return f'{name} aren\'t you a funny one'
    else:
        return '😵‍💫'
print('-'*20+"welcome to the chat bot!"+'-'*20)
name:str =input('what should i call you:')

print('-'*50)
try:
    while True:
        user_input:str =input(f'{name}:')

        if 'exit' in user_input:
            print(f'it was nice talking to you {name},bye-bye!👋')
            print('-' * 50)
            sys.exit()

        bot_response:str = get_response(user_input,name)
        print(f'bot:{bot_response}')
except KeyboardInterrupt:
    sys.exit()