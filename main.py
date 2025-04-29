from utils.model import users
from utils.controller import get_user_info, add_user, remove_user, edit_user


def main():
    print(f'Witaj {users[0]['name']}')

    while True:
        print('===========MENU===========')
        print('0 - zakończ program')
        print('1 - pokaż co u znajomych')
        print('2 - dodaj nowego znajomego')
        print('3 - usuń znajomego')
        print('4 - edytuj znajomego')
        print('==========================')
        choice = input('wybierz opcję MENU: ')
        if choice == '0': break
        if choice == '1': get_user_info(users[1:])
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': edit_user(users)


if __name__ == '__main__':
    main()

