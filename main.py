users:list=[
    {'name':'Franek','location':'Lublin','posts':2},
    {'name':'Oliwier','location':'Zamość','posts':3},
    {'name':'Kuba','location':'Warszawa','posts':500},
    {'name':'Konrad','location':'Lublin','posts':10},
]



def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów.')

get_user_info(users)