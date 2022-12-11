# part of the program
from utils.functions import Business, get_all_categorys, get_all_locations
from pathlib import Path  # for creating the Url and Api key input file
from time import sleep


if __name__ == '__main__':
    # for more information on maniualy adding the url and api key of Yelp API go to line 286 Or follow the steps in the Url and Api Key.txt file after it is created
    url = ''  # paste the url of your application
    api_key = ''  # paste the api key of your application

    # creating the file for api key and url from the user
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
        print('''The app will close itself (via automatic error) in 20s, this is necessery because You need to defy the api key and url of tihis aplication.
        To do this: Open the "Url and Api Key.txt" file located in the YelpBusinessSearch directory and follow the steps in it''')
        sleep(20)
        raise '''This restart was necessery
              Open the "Url and Api Key.txt" file and follow the steps in it'''  # the app needs to restart after creating the Url and Api Key file
    else:
        url_and_apikey_file_input = str(
            Path('Url and Api Key.txt').read_text())
        url_and_apikey_file_items = []

        # finding the url and api key in the file
        for i in url_and_apikey_file_input.split("'"):
            url_and_apikey_file_items.append(i)

        # implementing the url and api key from the save file
        url = url_and_apikey_file_items[1]
        api_key = url_and_apikey_file_items[3]

    # getting all possible Yelp category and location options
    category_names = get_all_categorys()
    location_names = get_all_locations()

    # choosing a valid category
    true_category = False
    while True:
        if true_category == True:
            break

        category = input(f'Choose the business category: ')
        if category in category_names:
            true_category = True

        else:
            print(f'''
        Invalid category, you can choose between:
        {category_names}
        ''')
            # checking for similar categorys if the category doesen't exist
            for category_ in category_names:
                if category in category_:
                    user_choice = input(
                        f'Did you mean {category_}? (y/n)')
                    if user_choice.lower() == 'y':
                        category = category_
                        true_category = True
                        break
                    else:
                        pass
                else:
                    pass

    # choosing a valid location
    true_location = False
    while True:
        if true_location == True:
            break

        location = input(f'Choose your business location: ')
        if location in location_names:
            true_location = True

        else:
            print(f'''
        Invalid category, you can choose between:
        {location_names}
            ''')
            # checking for similar locations if the location doesen't exist
            for location_ in location_names:
                if location in location_:
                    user_choice = input(
                        f'Did you mean {location_}? (y/n)')
                    if user_choice.lower() == 'y':
                        location = location_
                        true_location = True
                        break
                    else:
                        pass
                else:
                    pass

    # using the api key and url
    business = Business(url, api_key)

    end = False
    while True:
        if end == True:
            break

        else:
            question = input(
                'What do you want to know? (choose: name search(NS)/general search(GS)) ')

            if question.upper() == 'NS':
                while True:
                    business_name = input('Buisness name: ')
                    business.see_original_name(
                        business_name, category, location)
                    change = input(
                        'Change location, category, mode(name search or general search) or end app? (y/n)')

                    if change.lower() == 'y':
                        # end program?
                        end_program = input('end? (y/n) ')
                        if end_program.lower() == 'y':
                            end = True
                            break
                        else:
                            # choosing the name search or general serch again
                            change_nsgs = input(
                                'Change mode = (name search or general search)? (y/n)')
                            if change_nsgs.lower() == 'y':
                                break
                            else:
                                # choosing a valid category
                                true_category = False
                                while True:
                                    if true_category == True:
                                        break

                                    category = input(
                                        f'Choose the business category: ')
                                    if category in category_names:
                                        true_category = True

                                    else:
                                        print(f'''
                                    Invalid category, you can choose between:
                                    {category_names}
                                    ''')
                                        # checking for similar categorys if the category doesen't exist
                                        for category_ in category_names:
                                            if category in category_:
                                                user_choice = input(
                                                    f'Did you mean {category_}? (y/n)')
                                                if user_choice.lower() == 'y':
                                                    category = category_
                                                    true_category = True
                                                    break
                                                else:
                                                    pass
                                            else:
                                                pass

                                # choosing a valid location
                                true_location = False
                                while True:
                                    if true_location == True:
                                        break

                                    location = input(
                                        f'Choose your business location: ')
                                    if location in location_names:
                                        true_location = True

                                    else:
                                        print(f'''
                                    Invalid category, you can choose between:
                                    {location_names}
                                        ''')
                                        # checking for similar locations if the location doesen't exist
                                        for location_ in location_names:
                                            if location in location_:
                                                user_choice = input(
                                                    f'Did you mean {location_}? (y/n)')
                                                if user_choice.lower() == 'y':
                                                    location = location_
                                                    true_location = True
                                                    break
                                                else:
                                                    pass
                                            else:
                                                pass

            elif question.upper() == 'GS':
                valid_options = ['name', 'id', 'url', 'alias',
                                 'rating']
                while True:
                    # choosing a mode
                    mode = input(
                        'Choose a search mode: (name, id, url, alias, rating) ')

                    # checking if the choosen mode is valid
                    if mode.lower() in valid_options:
                        business.show_buisnesses(mode, category, location)

                        change = input(
                            'Change location, category, mode(name search or general search) or end app? (y/n)')
                        if change.lower() == 'y':
                            # end program?
                            end_program = input('end? (y/n) ')
                            if end_program.lower() == 'y':
                                end = True
                                break
                            else:
                                # choosing the name search or general serch again
                                change_nsgs = input(
                                    'Change mode = (name search or general search)? (y/n)')
                                if change_nsgs.lower() == 'y':
                                    break
                                else:
                                    # choosing a valid category
                                    true_category = False
                                    while True:
                                        if true_category == True:
                                            break

                                        category = input(
                                            f'Choose the business category: ')
                                        if category in category_names:
                                            true_category = True

                                        else:
                                            print(f'''
                                        Invalid category, you can choose between:
                                        {category_names}
                                        ''')
                                            # checking for similar categorys if the category doesen't exist
                                            for category_ in category_names:
                                                if category in category_:
                                                    user_choice = input(
                                                        f'Did you mean {category_}? (y/n)')
                                                    if user_choice.lower() == 'y':
                                                        category = category_
                                                        true_category = True
                                                        break
                                                    else:
                                                        pass
                                                else:
                                                    pass

                                    # choosing a valid location
                                    true_location = False
                                    while True:
                                        if true_location == True:
                                            break

                                        location = input(
                                            f'Choose your business location: ')
                                        if location in location_names:
                                            true_location = True

                                        else:
                                            print(f'''
                                        Invalid category, you can choose between:
                                        {location_names}
                                            ''')
                                            # checking for similar locations if the location doesen't exist
                                            for location_ in location_names:
                                                if location in location_:
                                                    user_choice = input(
                                                        f'Did you mean {location_}? (y/n)')
                                                    if user_choice.lower() == 'y':
                                                        location = location_
                                                        true_location = True
                                                        break
                                                    else:
                                                        pass
                                                else:
                                                    pass
                    else:
                        print(f'{mode} is not a valid option')
            else:
                print('Invalid Command')

    #
    #    For more information on how to create a yelp app go to:
    #    https://www.youtube.com/watch?v=GFhGN36Wf7Q a video by Widget Pack
    #    from there copy the api key and paste it in the quotations of api_key = '' on line 70
    #
    #   For the url go to Yelp Fusion> Business Endpoints> Business Search and copy the url after 'GET'
    #   then paste it in the quotations of url = '' on line 69
    #
