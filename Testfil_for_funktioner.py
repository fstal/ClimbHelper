import time

a = "fiSt"
a = a.capitalize()
print(a)


def menu():
    """
    Menu function, takes user input and calls different functions depending on it
    """
    print("Welcome to ClimbHelper! What would you like to do?")
    time.sleep(1)
    choice = input('1. Browse, 2. Search, 3. Adv. Search, 4. Add site, 5. Remove site, 6. Quit')
    while choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid input, please try again.")
        choice = input('1. Browse, 2. Search, 3. Adv. Search, 4. Add site, 5. Remove site, 6. Quit')
    choice = int(choice)
    if choice == 1:
        browse_climbing_sites()

    elif choice == 2:
        search_name = input('Enter the name of the site that you want to browse: ').capitalize()
        search_site()

    elif choice == 3:
        # take search parameters
        adv_search()

    elif choice == 4:
        add_climbsite()

    elif choice == 5:
        remove_input = input('Which site would you like to remove?: ').capitalize()
        removeSite(remove_input)

    elif choice == 6:
        file_saver()
        quit()


def removeSite(remove_input):
    found = False
    for i in obj_list:
        if i.name == remove_input:
            found = True
            are_you_sure = input('Are you sure that you want to remove ', remove_input, '? This action can not be undone. (Y/N): ').lower
            if are_you_sure in ['yes', 'y', 'no', 'n']:
                obj_list.remove(i)
                print('The site ', remove_input, ' was successfully deleted.')
                menu()
    if found is False:
        print('No such site was found... returning to menu')
        menu()


def addSiteName(new_site_name):
    while not all(c.isalpha() or c.isspace() for c in new_site_name) \
            and not any(c.isalpha() for c in new_site_name) \
            and not 2 < len(new_site_name) < 26:
        print('Invalid input, try again')
        new_site_name = input("Name your new climbing site (max 25 chars): ")
        # // validates that input is alphabetcial and 2-25 chars long, minst en bokstav
    new_site_name = new_site_name.capitalize()
    return  new_site_name


def addSiteIndoor(new_site_indoor):
    while new_site_indoor not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        new_site_indoor = input("Is there indoor climbing? (Yes/No): ").lower()
    if new_site_indoor in ['ja', 'j']:
        new_site_indoor = True
    else:
        new_site_indoor = False
        # // validates that input is yes/no, creates bool
    return new_site_indoor


def addSiteOutdoor(new_site_outdoor):
    while new_site_outdoor not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        new_site_outdoor = input("Is there outdoor climbing? (Yes/No): ").lower()
    if new_site_outdoor in ['yes', 'y']:
        new_site_outdoor = True
    else:
        new_site_outdoor = False
        # // validates that input is yes/no, creates bool
    return new_site_outdoor


def addSiteBouldering(new_site_bouldering):
    while new_site_bouldering not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        new_site_bouldering = input("Does the site have bouldering? (Yes/No): ").lower()
    if new_site_bouldering in ["yes", "y"]:
        new_site_bouldering = True
    else:
        new_site_bouldering = False
        # //validates that input is yes/no, creates bool
    return new_site_bouldering


def addSiteTop(new_site_top):
    while new_site_top not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        new_site_top = input("Is there top rope climbing? (Yes/No): ").lower()
    if new_site_top in ["yes", "y"]:
        new_site_top = True
    else:
        new_site_top = False
        # // validates that input is yes/no, creates bool
    return new_site_top


def addSiteCoords(new_site_coords):
    while not re.match("^[0-9]{1,3}[.][0-9]{3,25}[,][0-9]{1,3}[.][0-9]{3,25}$", new_site_coords):
        print('Invalid input, try again')
        new_site_coords = input("Please input the coordinates of the site (e.g 12.1234567,12.12345670000001): ")
    return new_site_coords


def addSiteDiffs(new_site_diffs):
    while not re.match("^[3-9][abc+-]{0,1}[\s][3-9][abc+-]{0,1}[\s][3-9][abc+-]{0,1}$", new_site_diffs):
        # måste lösa detta upplägg ovan
        print('Invalid input, try again')
        new_site_diffs = input("Which difficulties are there? (e.g. 4 5 7 - separated by whitespaces): ")
    new_site_diffs = new_site_diffs.split()
    singles = []
    for r in new_site_diffs:
        if r not in singles:
            singles.extend(r)
    new_site_diffs = singles
    new_site_diffs.sort()
    # // Validerar först input
    # // Gör string till lista med split()
    # // Ser till att ta bort dubletter ur listinnehåll
    # // Sorterar lista
    return new_site_diffs


def addSiteDesc(new_site_desc):
    while not len(new_site_desc) < 101:
        print('Invalid input, try again')
        new_site_desc = input("Kindly provide a short description of the site, max 100 characters: ")
        # // validates that input is less than 100 chars, can contain non-alpha
    return new_site_desc


def addClimbSite():
    """
    :return:
    """
    new_site_name = input("Name your new climbing site (max 25 chars): ").lower()
    name = addSiteName(new_site_name)

    new_site_indoor = input("Is there indoor climbing? (Yes/No): ").lower()
    indoor = addSiteIndoor(new_site_indoor)

    new_site_outdoor = input("Is there outdoor climbing? (Yes/No): ").lower()
    outdoor = addSiteOutdoor(new_site_outdoor)

    new_site_bouldering = input("Does the site have bouldering? (Yes/No): ").lower()
    bouldering = addSiteBouldering(new_site_bouldering)

    new_site_top = input("Is there top rope climbing? (Yes/No): ").lower()
    top = addSiteTop(new_site_top)

    new_site_coords = input("Please input the coordinates of the site (e.g 12.1234567,12.12345670000001): ")
    coords = addSiteCoords(new_site_coords)

    new_site_diffs = input("Which difficulties are there? (e.g. 4 5 7 - separated by whitespaces): ")
    diffs = addSiteDiffs(new_site_diffs)

    new_site_desc = input("Kindly provide a short description of the site, max 100 characters: ")
    desc = addSiteDesc(new_site_desc)

    new_climbsite = ClimbSite(name, indoor, outdoor, bouldering, top, coords, diffs, desc)
    obj_list.append(new_climbsite)
    print(new_climbsite.name, ' was successfully added to the as a new climbing site! Returning to main menu...')
    menu()


def advSearch():

    advSearchHelper()
    advSearchParameters()

def advSearchHelper():
    print('Combine numbers in a sequence to decide which parameters you want to include in your search')
    print(' 1 = Indoor \n 2 = Outdoor \n 3 = Bouldering \n 4 = Toprope \n 5 = Difficulties')
    print('Eg. "236" to include in your search: whether there is indoor and outdoor climbing as well as specific difficulties')
    adv_search_seq = input('Enter your sequence: ')
    while not 1 < len(adv_search_seq) < 6 and
        not in ['1', '2', '3', '4', '5']  # inte inkludera flera av samma siffra stripa den siffran då
        print('Invalid input, try again')
        adv_search_seq = input('Enter your sequence: ')


    if


    advSearchParameters(adv_search_seq)

def advSearchParameters(adv_search_seq):
    adv_search_indoor = None
    adv_search_outdoor = None
    adv_search_bouldering = None
    adv_search_top = None
    adv_search_diffs = None

    for i in adv_search_seq:
        if i == '1':
            adv_search_indoor = True
        elif i == '2':
            adv_search_outdoor = True
        elif i == '3':
            adv_search_bouldering = True
        elif i == '4':
            adv_search_top = True
        elif i == '5':
            adv_search_diffs = input('Which difficulties do you require the site to have? (e.g. 4 5 7 - separated by whitespaces): ')

def actualSearchAndPrint():
    print_list = []
    for obj in obj_list:
        if all(obj.indoor is adv)


        if adv_search_indoor is not None:


          #      obj:

            print_list.append(obj)
    if len(print_list) > 1:
        print('Sorry, no matching results. Returning to main menu...')
        menu()
    else:
        print('\n The following sites matched your search criteria')
        for i in print_list:
            print(i)
            print('')


    for x in abc_list:
        if x is not None:
            abcd_list.append(x)


        while not all(c.isalpha() or c.isspace() for c in new_site_name) \
                and not any(c.isalpha() for c in new_site_name) \
                and not 2 < len(new_site_name) < 26:
            print('Invalid input, try again')
            new_site_name = input("Name your new climbing site (max 25 chars): ")
        new_site_name = new_site_name.capitalize()
        return new_site_name





























def advBrowse():
    a

    advBrowse_input = input('')

