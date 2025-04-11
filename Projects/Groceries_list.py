import sys

def welcome_message() -> None:
    print('-'*20+' Welcome to Groceries list!📃 '+'-'*20)
    print(' '*47)
    print('+'+'-'*10+' Options: '+'-'*10+'+')
    print('\'1\' To add an item.\n'
          '\'2\' To remove an item\n'
          '\'3\' To list all items\n'
          '\'4\' Edit the list\n'
          '\'0\' To exit the program')
    print('+'+'-'*30+'+')

def add_item(item:str,groceries_list:list[str]) -> None:
    if item != ' ':
        groceries_list.append(item)
        print(f'\'{item}\' added to the list!')
    else:
        print('what do you want to add the void?🙄')

def remove_item(item:str,groceries_list:list[str]) -> None:
    try:
        groceries_list.remove(item)
        print(f'\'{item}\' removed from the list!')
    except ValueError:
        print(f'\'{item}\' not found in the list!...')

def display(groceries_list:list[str]) -> None:
    print('+'+'-'*5+' List📃 '+'-'*5+'+')
    if groceries_list:
        for i,v in enumerate(groceries_list,1):
            print(f'{i}: {v.capitalize()}')
    else:
        print('the list is empty...')
    print('+' + '-' * 18 + '+')

def is_valid_option(text:str) -> bool:
    return text in ['0','1','2','3','4']

def edit_list(position:int,new_item:str,groceries_list:list[str]) -> None:
    try:
        if len(groceries_list)>= int(position) > 0:
            groceries_list[int(position)-1] = new_item
            print(f'{new_item} added at {position}!')
        else:
            print('invalid position!...')
    except ValueError:
        print('invalid position!...')

def main() -> None:
    groceries_list: list[str] = []
    welcome_message()
    while True:
        user_input:str= input('select an option:').lower()

        if not is_valid_option(user_input):
            print('not a valid option...')
            continue
        elif user_input=='1':
            item:str = input('enter the item to be added >>> ')
            add_item(item,groceries_list)
        elif user_input == '2':
            item:str = input('enter the item to be removed >>> ')
            remove_item(item,groceries_list)
        elif user_input == '3':
            display(groceries_list)
        elif user_input == '4':
            position:int = input('enter the position to edit >>> ')
            new_item:str= input('enter the new item >>> ')
            edit_list(position,new_item,groceries_list)
        elif user_input == '0':
            print(f'bye-bye!...')
            sys.exit()


if __name__ == '__main__':
    main()