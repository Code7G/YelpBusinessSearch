import requests  # for sending requests to Yelp API
from pathlib import Path  # for creating the Url and Api key input file


class Business:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def see_original_name(self, business_name, category, location):
        headers = {'Authorization': 'Bearer ' + api_key}
        params = {'term': category, 'location': location}
        response = requests.get(url, headers=headers, params=params)
        businesses = response.json()['businesses']

        names = []

        # getting all the names
        [names.append(business['name']) for business in businesses]

        # searching if the given name already exists
        if business_name in names:
            print(f'The name {business_name} has already been taken')
        else:
            # for showing similar names
            for name in names:
                if business_name in name:
                    print(f'Similar name: {name}')
            print('Your name is original!')

    def show_buisnesses(self, category, location):
        headers = {'Authorization': 'Bearer ' + api_key}
        params = {'term': category, 'location': location}
        response = requests.get(url, headers=headers, params=params)
        businesses = response.json()['businesses']

        print(f'Here are all {category} busnesses in {location}:')

        # printing all the business names
        for business in businesses:
            print(business['name'])


category = input('Buisness category: ')
location = input('Buisness location: ')

# for more information on maniualy adding the url and api key of Yelp go to line 116
url = ''  # paste the url of your application
api_key = ''  # paste the api key of your application

url_and_apikey_file = Path('Url and Api Key.txt')
if url_and_apikey_file.exists() == False:
    Path('Url and Api Key.txt').write_text('''
    App Url: ''
    App Api Key: ''
    
    Paste the url and api key in the quotations
    
    For more information on how to create a yelp app go to:
    https://www.youtube.com/watch?v=GFhGN36Wf7Q a video by Widget Pack
    from there copy the api key
    
    For the url go to Yelp Fusion> Business Endpoints> Business Search and copy the url after 'GET'
    ''')
    raise 'This restart was necessery. Open the "Url and Api Key.txt" file and follow the steps in it'  # the app needs to restart after creating the Url and Api Key file
else:
    url_and_apikey_file_input = str(Path('Url and Api Key.txt').read_text())
    url_and_apikey_file_items = []

    # finding the url and api key in the file
    for i in url_and_apikey_file_input.split("'"):
        url_and_apikey_file_items.append(i)

    # implementing the url and api key from the save file
    url = url_and_apikey_file_items[1]
    api_key = url_and_apikey_file_items[3]


question = input('See if your buisness name is original? (y/n) ')

business = Business(url, api_key)

if question == 'y':
    while True:
        business_name = input('Buisness name: ')
        business.see_original_name(business_name, category, location)
        change = input('Change location or category? (y/n)')
        if change == 'y':
            category = input('Buisness category: ')
            location = input('Buisness location: ')
        else:
            end_program = input('end? (y/n) ')
            if end_program == 'y':
                break
            else:
                pass
else:
    while True:
        business.show_buisnesses(category, location)
        change = input('Change location or category? (y/n)')
        if change == 'y':
            category = input('Buisness category: ')
            location = input('Buisness location: ')
        else:
            end_program = input('end? (y/n) ')
            if end_program == 'y':
                break
            else:
                pass

#
#    For more information on how to create a yelp app go to:
#    https://www.youtube.com/watch?v=GFhGN36Wf7Q a video by Widget Pack
#    from there copy the api key and paste it in the quotations of api_key = '' on line 54
#
#   For the url go to Yelp Fusion> Business Endpoints> Business Search and copy the url after 'GET'
#   then paste it in the quotations of url = '' on line 53
#
