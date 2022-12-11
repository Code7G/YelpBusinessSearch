from requests import request  # for sending requests to the Yelp API
from pathlib import Path  # for accesing the categorys and locations files in utils


class Business:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def send_valid_request(self, category, location):
        headers = {'Authorization': 'Bearer ' + self.api_key}
        params = {'term': category, 'location': location}
        response = request('GET', self.url, params=params, headers=headers)
        businesses = response.json()['businesses']
        return businesses

    def see_original_name(self, business_name, category, location):
        businesses = self.send_valid_request(category, location)

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

    def show_buisnesses(self, mode, category, location):
        businesses = self.send_valid_request(category, location)

        print(f'Here are all {category} busnesses in {location} by {mode}:')

        # printing all the business names and thair choosen factor
        # example: (name of business) (example:rating) = (example:4.5)
        # final resoult: Restaurant rating = 4.5
        for business in businesses:
            print(f'{business["name"]} {mode} = {business[mode]}')


def get_all_categorys():
    # get the text data of the categorys file
    categorys = Path('utils/categorys.txt').read_text()

    # separate the categorys by '\n' (the end of a line in the file) and individually append them to a list
    category_list = []
    for category in categorys.split('\n'):
        category_list.append(category)

    return category_list


def get_all_locations():
    # get the text data of the locations file
    locations = Path('utils/locations.txt').read_text()

    # separate the locations by '\n' (the end of a line in the file) and individually append them to a list
    location_list = []
    for location in locations.split('\n'):
        location_list.append(location)

    return location_list

# source of all the Yelp categorys: https://blog.yelp.com/businesses/yelp_category_list/
# source of all the Yelp locations: https://www.yelp.com/locations
