def get_sports(sport: str):
    return sport

def get_coaches(name: str):
    return coaches[name], name

def get_schedules(sport: str):
    return schedule[sport]

def get_prices(sport: str):
    return prices.get(sport)

sports = ["football", "basketball", "Tennis"]

coaches = {'Arteta': 'football', 'Kid': 'basketball', 'Leon': 'Tennis',}

schedule = {
    "football": ["Monday 18:00", "Wednesday 18:00", "Friday 18:00"],
    "basketball": ["Monday 19:00", "Saturday 19:00"],
    "Tennis": ["Wednesday 17:00", "Friday 17:00"],
    }

prices = {"football": "$150", "basketball": "$120", "Tennis": "$100",}


print('1 - football \n2 - basketball \n3 - tennis \n4 - exit')
while True:
    try:
        sport_choice = input('Choose your sport: ')

        if sport_choice == '4':
            print('Have a good day')
            break

        elif sport_choice == '1':
            name_coach = get_coaches('Arteta')
            print(f'Coach name - {name_coach[1]}. \nSport - {name_coach[0]}')
            print('Training days -', get_schedules(name_coach[0]))
            print('Training price -', get_prices(name_coach[0]))
 
        elif sport_choice == '2':
            name_coach = get_coaches('Kid')
            print(f'Coach name - {name_coach[1]}. \nSport - {name_coach[0]}')
            print('Training days -', get_schedules(name_coach[0]))
            print('Training price -', get_prices(name_coach[0]))

        elif sport_choice == '3':
            name_coach = get_coaches('Leon')
            print(f'Coach name - {name_coach[1]}. \nSport - {name_coach[0]}')
            print('Training days -', get_schedules(name_coach[0]))
            print('Training price -', get_prices(name_coach[0]))

    except KeyError as K:
        print(f'Coach {K} not found')
        break


