from datetime import datetime, timedelta
from random import choice

class Chatbot:
    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age
        self.start_time:datetime = datetime.now()

    def describe(self)->None:
        print(f'This is a chatbot called {self.name} it\'s {self.age} years old.')

    def get_response(self,txt:str)->str:
        lowered = txt.lower()
        if 'hello' in lowered:
            return f'{self.name}: hey there!!😊'
        elif 'time' in lowered:
            time:datetime = datetime.now()
            elapsed_time:datetime = time - self.start_time
            return f'{self.name}: the current time is {time:%H:%M:%S} ⌚{f'\nit has been {elapsed_time.seconds} minutes since you have been talking to me go touch grass 🌿' if elapsed_time > timedelta(minutes=1) else ' '}'
        elif 'how old are you' in lowered:
            return f'{self.name}: im {self.age} years old'
        elif 'bye' in lowered:
            return f'{self.name}: see you!! 👋'
        else:
            yap:list[str]=['🙄','😭',
                           'i dont speak gen z',
                           'idk i just got here','😵‍💫','😒',
                           'please try re-phrasing','🤖','(⊙_⊙)?','what the sigma!'
                           ,'oie-a 🐈','(┬┬﹏┬┬)','(╯▔皿▔)╯','yeah, yeah','ahh, what?']
            return f'{self.name}: {choice(yap)}'

    def run(self)->None:
        while True:
            user_input:str = input('you: ')
            if user_input.lower().strip() == 'exit':
                print(f'thank you for talking with {self.name}')
                break
            else:
                responses:str = self.get_response(user_input)
                print(f'{responses}')

def main() -> None:
    try:
        joi:Chatbot = Chatbot('JOI',22)
        joi.describe()
        joi.run()
    except KeyboardInterrupt:
        print('\nbye-bye!')
    except Exception as e:
        print(f'encountered exception {e}')

if __name__ == '__main__':
    main()
#