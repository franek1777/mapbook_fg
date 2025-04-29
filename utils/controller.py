def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów.')


def add_user(users_data: list) -> None:
    new_name = input('podaj imie nowego znajomego: ')
    new_location = input('podaj miasto pochodzenia nowego znajomego: ')
    new_posts = int(input('podaj ilość postów nowego znajomego: '))
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts})


def remove_user(users_data: list) -> None:
    user_tbr = input('podaj nazwę znajomego do usunięcia: ')
    for user in users_data:
        if user['name'] == user_tbr:
            users_data.remove(user)


def edit_user(users_data: list) -> None:
    user_tbe = input('podaj nazwę znajomego do edycji: ')
    for user in users_data:
        if user['name'] == user_tbe:
            user['name'] = input('podaj nowe imie: ')
            user['location'] = input('podaj nową lokalizacje: ')
            user['posts'] = input('podaj nową liczbę postów: ')