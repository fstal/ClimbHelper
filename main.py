from classes import ClimbSite
import sys
import re
import time


def filerReader():
    """
    filerReader() reads our file containing our climb sites and separates
    the different attributes to elements in a list
    :return:
    """
    with open('Climbing_spots.txt', 'r') as read:
        for row in read:
            row_list = row.split('<SEP>')
            list(map(str.strip, row_list))
            readFormater(row_list)
    print('Welcome to ClimbHelper! What would you like to do?')
    time.sleep(1)
    menu()


def readFormater(row_list):
    """
    readFormater() properly formats our elements in the read list preparing them to be made
    into objects. Creating proper booleans and lists withing the list.
    :param row_list:
    :return:
    """
    row_list_formated = [row_list[0]]
    row_list_bools = row_list[1:5]
    for i in row_list_bools:
        if i == "True":
            row_list_formated.append(True)
        else:
            row_list_formated.append(False)
    row_list_formated.append(row_list[5])
    row_list_formated.append(row_list[6].split())
    row_list_formated.append(row_list[7].rstrip('\n'))
    objectCreator(row_list_formated)


def objectCreator(row_list_formated):
    """
    objectCreator() simply makes our formated row_lists into objects
    and stores them in a list
    :param row_list_formated:
    :return:
    """
    created_site = ClimbSite(
        row_list_formated[0], row_list_formated[1], row_list_formated[2], row_list_formated[3],
        row_list_formated[4], row_list_formated[5], row_list_formated[6], row_list_formated[7])
    obj_list.append(created_site)


def fileSaver():
    """
    Called when the user tries to exit the program, sorts the objects and writes to file.
    :return:
    """
    obj_list.sort(key=lambda x: x.name, reverse=False)  # // sorts on obj.name
    writer = open("climbing_spots.txt", 'w')
    for obj in obj_list:
        writer.write(obj.name)
        writer.write("<SEP>")
        writer.write(str(obj.indoor))
        writer.write("<SEP>")
        writer.write(str(obj.outdoor))
        writer.write("<SEP>")
        writer.write(str(obj.bouldering))
        writer.write("<SEP>")
        writer.write(str(obj.top))
        writer.write("<SEP>")
        writer.write(obj.coords)
        writer.write("<SEP>")
        for k in obj.diffs:
            writer.write(k + ' ')
        writer.write("<SEP>")
        writer.write(obj.desc)
        writer.write("<SEP>")
        writer.write("\n")
    writer.close()


def menu():
    """
    Menu function, takes user input and calls different functions depending on the input
    """
    print('')
    choice = input('1. Browse all sites \n2. Search using name \n3. Advanced search \n4. Add a new climbing site '
                   '\n5. Remove site \n6. Quit \nInput: ')
    while choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid input, please try again.")
        choice = input('1. Browse all sites \n2. Search using name \n3. Advanced search \n4. Add a new climbing site '
                       '\n5. Remove site \n6. Quit \nInput: ')
    choice = int(choice)
    print('')
    if choice == 1:
        browseClimbingSites()

    elif choice == 2:
        search_name = input('Enter the name of the site that you want to browse: ').capitalize()
        searchSite(search_name)

    elif choice == 3:
        print('This function will ask you a few questions to better customize your search results')
        proceed = input('Do you want to proceed? (Y/N): ').lower()
        if proceed in ['n', 'no']:
            print('That is fine, returning to main menu.')
            menu()
        elif proceed in ['y', 'yes']:
            advSearch()
        else:
            print('Invalid input. Returning to main menu.')
            menu()

    elif choice == 4:
        addClimbSite()

    elif choice == 5:
        remove_input = input('Which site would you like to remove?: ')
        remove_input = remove_input.capitalize()
        removeSite(remove_input)

    elif choice == 6:
        fileSaver()
        print('Exiting program, be back soon!')
        sys.exit()


def browseClimbingSites():
    """
    list the names of all our sites
    """
    obj_list.sort(key=lambda x: x.name, reverse=False)  # // sorts on obj.name
    print('The following climbing sites currently exist in the database: \n')
    for obj in obj_list:
        print(obj.name)
    search_name = input('Enter the name of a site you want to examine further, or (r/return) to return to the main menu: ').capitalize()
    if search_name in ['Return', 'R']:
        menu()
    else:
        print('')
        searchSite(search_name)


def searchSite(search_name):
    """
    if user input equals the name attr of a ClimbSite
    prints information about that site
    :return:
    """
    for obj in obj_list:
        if search_name == obj.name:
            print(obj)
            break
    else:
        print("No climbing site with that name found... Returning to main menu.")
    menu()


def removeSite(remove_input):
    """
    if a ClimbSite object with a matching name attribute exist,
    Ask user to confirm the deletion of that object and executes
    :param remove_input:
    :return:
    """
    found = False
    for i in obj_list:
        if i.name == remove_input:
            found = True
            are_you_sure = input('Are you sure that you want to remove ' + str(remove_input) + '? This action can not be undone. (Y/N): ')
            are_you_sure = are_you_sure.lower()
            while are_you_sure not in ['yes', 'y', 'no', 'n']:
                print("Invalid input, please try again.")
                are_you_sure = input('Are you sure that you want to remove ' + str(remove_input) + '? This action can not be undone. (Y/N): ')
                are_you_sure = are_you_sure.lower()
            if are_you_sure in ['yes', 'y']:
                obj_list.remove(i)
                print('The site ', remove_input, ' was successfully deleted.')
                menu()
            else:
                print('Very well. Returning to main menu...')
                menu()
    if found is False:
        print('No such site was found... returning to menu')
        menu()


def addClimbSite():
    """
    Creates a new ClimbSite-object based on user input.
    Calls for a input validation function for each attribute
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


def addSiteName(new_site_name):
    """
    Input and string validation for name-attribute
    * Alphabetical and spaces, 2-25 chars long, at least one alpha. Also checks for name duplicates
    :param new_site_name:
    :return:
    """
    while not all(c.isalpha() or c.isspace() for c in new_site_name) \
            and not any(c.isalpha() for c in new_site_name) \
            and not 2 < len(new_site_name) < 26:
        print('Invalid input, try again')
        new_site_name = input("Name your new climbing site (max 25 chars): ").capitalize()
    if checkDuplicates(new_site_name) is True:
        return new_site_name
    else:
        print('Sorry, a climbing site with that name already exists. Returning to main menu.')
        menu()


def checkDuplicates(new_site_name):
    """
    Simple help function for making sure no two objects with the
    same name attribute exists
    :param new_site_name:
    :return:
    """
    duplicate_found = False
    for i in obj_list:
        if i.name == new_site_name:
            duplicate_found = True
            break
    return duplicate_found


def addSiteIndoor(new_site_indoor):
    """
    Input and string validation for indoor-attribute
    * Accepts 'yes', 'no', 'y', 'n' - Creates boolean
    :param new_site_indoor:
    :return:
    """
    while new_site_indoor not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        new_site_indoor = input("Is there indoor climbing? (Yes/No): ").lower()
    if new_site_indoor in ['yes', 'y']:
        new_site_indoor = True
    else:
        new_site_indoor = False
    return new_site_indoor


def addSiteOutdoor(new_site_outdoor):
    """
    Input and string validation for outdoor-attribute
    * Accepts 'yes', 'no', 'y', 'n' - Creates boolean
    :param new_site_outdoor:
    :return:
    """
    while new_site_outdoor not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        new_site_outdoor = input("Is there outdoor climbing? (Yes/No): ").lower()
    if new_site_outdoor in ['yes', 'y']:
        new_site_outdoor = True
    else:
        new_site_outdoor = False
    return new_site_outdoor


def addSiteBouldering(new_site_bouldering):
    """
    Input and string validation for indoor-bouldering
    * Accepts 'yes', 'no', 'y', 'n' - Creates boolean
    :param new_site_bouldering:
    :return:
    """
    while new_site_bouldering not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        new_site_bouldering = input("Does the site have bouldering? (Yes/No): ").lower()
    if new_site_bouldering in ["yes", "y"]:
        new_site_bouldering = True
    else:
        new_site_bouldering = False
    return new_site_bouldering


def addSiteTop(new_site_top):
    """
    Input and string validation for top-attribute
    * Accepts 'yes', 'no', 'y', 'n' - Creates boolean
    :param new_site_top:
    :return:
    """
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
    """
    Input and string validation for coords-attribute
    * Uses regular expressions to validate the format of the coordinates.
    :param new_site_coords:
    :return:
    """
    while not re.match("^[0-9]{1,3}[.][0-9]{3,25}[,][0-9]{1,3}[.][0-9]{3,25}$", new_site_coords):
        print('Invalid input, try again')
        new_site_coords = input("Please input the coordinates of the site (e.g 12.1234567,12.12345670000001): ")
    return new_site_coords


def addSiteDiffs(new_site_diffs):
    """
    Input and string validation for diffs-attribute
    Uses regex to validate input and removes duplicate difficulties
    Returns a list
    :param new_site_diffs:
    :return:
    """
    while not re.match(r'[[3-9][\s]]{1,5}[3-9]]|[3-9]', new_site_diffs):
        print('Invalid input, try again')
        new_site_diffs = input("Which difficulties? (e.g. 4 5 7 - separated by whitespaces): ")
    new_site_diffs = new_site_diffs.split()
    singles = []
    for r in new_site_diffs:
        if r not in singles:
            singles.extend(r)
    new_site_diffs = singles
    new_site_diffs.sort()
    return new_site_diffs


def addSiteDesc(new_site_desc):
    """
    Input and string validation for desc-attribute
    * Accepts mostly anything with a length less than 100 chars
    :param new_site_desc:
    :return:
    """
    while not len(new_site_desc) < 101:
        print('Invalid input, try again')
        new_site_desc = input("Kindly provide a short description of the site, max 100 characters: ")
        # // validates that input is less than 100 chars, can contain non-alpha
    return new_site_desc


def advSearch():
    """
    Attribute specific search that calls for a input validation function for each attribute
    :return:
    """
    p_indoor = advParameterIndoor()
    p_outdoor = advParameterOutdoor()
    p_bouldering = advParameterBouldering()
    p_top = advParameterTop()
    p_diffs = advParameterDiffs()
    print_list = checker(p_indoor, p_outdoor, p_bouldering, p_top, p_diffs)

    if len(print_list) < 1:
        print('\n Your search conditions returned no results. Returning to main menu')
        menu()
    else:
        print('Search results: \n')
        for p in print_list:
            print(p)
            print('')
        menu()


def advParameterIndoor():
    """

    :return:
    """
    param_indoor = input('Do you require your search to only include sites with indoor climbing? (Y/N): ').lower()
    while param_indoor not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        param_indoor = input('Do you require your search to only include sites with indoor climbing? (Y/N): ').lower()
    if param_indoor in ["yes", "y"]:
        param_indoor = True
    else:
        param_indoor = None
    return param_indoor


def advParameterOutdoor():
    param_outdoor = input('Do you require your search to only include sites with outdoor climbing? (Y/N): ').lower()
    while param_outdoor not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        param_outdoor = input('Do you require your search to only include sites with outdoor climbing? (Y/N): ').lower()
    if param_outdoor in ["yes", "y"]:
        param_outdoor = True
    else:
        param_outdoor = None
    return param_outdoor


def advParameterBouldering():
    param_bouldering = input('Do you require your search to only include sites with bouldering climbing? (Y/N): ').lower()
    while param_bouldering not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        param_bouldering = input('Do you require your search to only include sites with bouldering climbing? (Y/N): ').lower()
    if param_bouldering in ["yes", "y"]:
        param_bouldering = True
    else:
        param_bouldering = None
    return param_bouldering


def advParameterTop():
    param_top = input('Do you require your search to only include sites with top rope climbing? (Y/N): ').lower()
    while param_top not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        param_top = input('Do you require your search to only include sites with top rope climbing? (Y/N): ').lower()
    if param_top in ["yes", "y"]:
        param_top = True
    else:
        param_top = None
    return param_top


def advParameterDiffs():
    param_diffs = input('Do you require your search to only include sites with specific difficulties? (Y/N): ')
    while param_diffs not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        param_diffs = input('Do you require your search to only include sites with specific difficulties? (Y/N): ')
    if param_diffs in ["yes", "y"]:
        new_site_diffs = input("Which difficulties? (e.g. 4 5 7 - separated by whitespaces): ")
        param_diffs = addSiteDiffs(new_site_diffs)
    else:
        param_diffs = None
    return param_diffs


def checker(p_indoor, p_outdoor, p_bouldering, p_top, p_diffs):
    """
    The logic is simple:
    if the parameter variable is None, we dont care about this attribute, hence pass and check next attribute.
    If it is not None, we only want to accept it (pass) if the attribute is True.
    If its not True, continue to the next iteration in the loop.

    :param p_indoor:
    :param p_outdoor:
    :param p_bouldering:
    :param p_top:
    :param p_diffs:
    :return:
    """
    print_list = []
    for i in obj_list:
        if p_indoor is None:
            pass
        else:
            if i.indoor is True:
                pass
            else:
                continue

        if p_outdoor is None:
            pass
        else:
            if i.outdoor is True:
                pass
            else:
                continue

        if p_bouldering is None:
            pass
        else:
            if i.bouldering is True:
                pass
            else:
                continue

        if p_top is None:
            pass
        else:
            if i.itop is True:
                pass
            else:
                continue

        if p_diffs is None:
            pass
        else:
            failed = False
            for g in p_diffs:
                if g not in i.diffs:
                    failed = True
            if failed:
                continue
            else:
                pass

        print_list.append(i)
    return print_list


obj_list = []
filerReader()


"""
om jag vill använda det andra svårighetssystemet:
    while not re.match("^[3-9][abc+-]{0,1}[\s][3-9][abc+-]{0,1}[\s][3-9][abc+-]{0,1}$", new_site_diffs): ish

att göra:
generealisera bort
lägga till fler climbing spots

advParameterIndoor
advParameterOutdoor
advParameterBouldering
advParameterTop



"""
