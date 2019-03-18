from classes import ClimbSite


alist = ['1','2','3','4','5']
for i in alist:
    if i == "2":
        pass
    else:
        print(i)

"""
hol = ClimbSite('Asdklippan', True, True, True, True, "123.12315,123.12344", [4,5,6,7], 'fisk')
if hol.name:
    print('godis')

if gid:
    print('shit')

#a, b, c, d, e, f, g = 0
#print(c)
a, b, c, d, e, f, g = None, None, None, None, None, None, None,

"""
a = None
b = None
c = None
d = None
e = None
f = None
g = None
"""
print('1 Name \n 2 = Indoor \n 3 = Outdoor \n 4 = Bouldering \n 5 = Toprope \n 6 = Difficulties')

print(a)
print(b)


def paramBrowse():
    print('This function will ask you a few questions to better customize your search results')
    proceed = input('Do you want to proceed? (Y/N)').lower()
    if proceed in ['n', 'no']:
        print('That is fine, returning to main menu.')
        menu()
    elif proceed in ['y', 'yes']:
        paramBrowseHelp()
    else:
        print('Invalid input. Returning to main menu.')
        menu()


def paramBrowseHelp():
    param_indoor = input('Do you require your search to only include sites with indoor climbing? (Y/N): ').lower()
    while param_indoor not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        param_indoor = input('Do you require your search to only include sites with indoor climbing? (Y/N): ').lower()
    if param_indoor in ["yes", "y"]:
        param_indoor = True
    else:
        param_indoor = None

    param_outdoor = input('Do you require your search to only include sites with outdoor climbing? (Y/N): ').lower()
    while param_outdoor not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        param_outdoor = input('Do you require your search to only include sites with outdoor climbing? (Y/N): ').lower()
    if param_outdoor in ["yes", "y"]:
        param_outdoor = True
    else:
        param_indoor = None

    param_bouldering = input('Do you require your search to only include sites with bouldering climbing? (Y/N): ').lower()
    while param_bouldering not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        param_bouldering = input('Do you require your search to only include sites with bouldering climbing? (Y/N): ').lower()
    if param_bouldering in ["yes", "y"]:
        param_bouldering = True
    else:
        param_indoor = None

    param_top = input('Do you require your search to only include sites with top rope climbing? (Y/N): ').lower()
    while param_top not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        param_top = input('Do you require your search to only include sites with top rope climbing? (Y/N): ').lower()
    if param_top in ["yes", "y"]:
        param_top = True
    else:
        param_top = None

    param_diffs = input('Do you require your search to only include sites with specific difficulties? (Y/N): ')
    while param_diffs not in ['yes', 'y', 'no', 'n']:
        print('Invalid input, try again')
        param_diffs = input('Do you require your search to only include sites with specific difficulties? (Y/N): ')
    if param_diffs in ["yes", "y"]:
        new_site_diffs = input("Which difficulties? (e.g. 4 5 7 - separated by whitespaces): ")
        param_diffs = addSiteDiffs(new_site_diffs)
    else:
        param_diffs = None

    checker(param_indoor, param_outdoor, param_bouldering, param_top, param_diffs)


def checker(param_indoor, param_outdoor, param_bouldering, param_top, param_diffs):
    print_list = []
    for i in obj_list:
        if param_indoor is None:
            pass
        else:
            if i.indoor is True:
                pass
            else:
                continue

        if param_outdoor is None:
            pass
        else:
            if i.outdoor is True:
                pass
            else:
                continue

        if param_bouldering is None:
            pass
        else:
            if i.bouldering is True:
                pass
            else:
                continue

        if param_top is None:
            pass
        else:
            if i.itop is True:
                pass
            else:
                continue

        if param_diffs is None:
            pass
        else:
            for g in param_diffs:
                if g in i.diffs:
                    pass
                else:
                    continue

        print_list.append(i)
    return print_list

    print('Search results: ')
    print('')
    for p in print_list:
        print(p)
        print('')
    menu()



    def xyHelper(x, y):
        x = input('Do you require your search to only include sites with ' + y + '? (Y/N): ')
        while x not in ['yes', 'y', 'no', 'n']:
            print('Invalid input, try again')
            x = input("Is there top rope climbing? (Yes/No): ").lower()
        if x in ["yes", "y"]:
            x = True
        else:
            x = None
        return x

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

while new_site_indoor not in ['yes', 'y', 'no', 'n']:
    print('Invalid input, try again')
    new_site_indoor = input("Is there indoor climbing? (Yes/No): ").lower()
if new_site_indoor in ['y', 'yes']:
    new_site_indoor = True
else:
    new_site_indoor = False
return new_site_indoor
