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

            def get_cordinates(city: str) -> list:
                import requests
                from bs4 import BeautifulSoup
                url = f'https://pl.wikipedia.org/wiki/{city}'
                response = requests.get(url).text
                response_html = BeautifulSoup(response, 'html.parser')
                longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
                latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
                print(longitude, latitude)
                return latitude, longitude

            def get_map(users_data: list) -> None:
                import folium
                map = folium.Map(location=(52.23, 21.00), zoom_start=6)

                for user in users:
                    cordinates = get_cordinates(user['location'])
                    folium.Marker(location=cordinates, popup=f'{user['location']}<br/>{user['name']}').add_to(map)
                map.save('mapa.html')