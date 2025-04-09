from utils.model import users
from utils.controller import get_user_info


def main():
    print(f'Witaj {users[0]['name']}')

    while True:
        print('============MENU==========')
        print('0 - zakończ program')
        print('1 - pokaż co u znajomych')
        print('============MENU==========')
        choice=input('wybierz opcje MENU: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)
    get_user_info(users)


if __name__ == '__main__':
    main()