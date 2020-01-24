import requests


while True:
    
    s_city = input('Enter city and country(optional): ')
    city_id = 0
    appid = 'c40caff3ffe9339e82e958a0f6e07a32'
    
    try:
        res = requests.get('http://api.openweathermap.org/data/2.5/find',
        params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        for city in data['list']:
            print(
                f'id: {city["id"]}\n',
                f'   name: {city["name"]}\n',
                f'   temp: {city["main"]["temp"]}\n',
                f'   pressure: {city["main"]["pressure"]}\n',
                f'   humidity: {city["main"]["humidity"]}\n',
            )
    
    except Exception as e:
        print('Exception (find):', e)
        pass