from Person import Person
import operator, os


# Läser in fil och lagrar i lista
def readFile(filename, personlist):
    try:
        file = open(filename, "r")
        while True:
            familyname = file.readline().strip('\n')
            if not familyname: break
            name = file.readline().strip('\n')
            number = file.readline().strip('\n')
            address = file.readline().strip('\n')
            newperson = Person(familyname, name, number, address)
            personlist.append(newperson)
        file.close()
    except (IOError, EOFError)as e:
        print(e)


# Sparar lista med personer i en fil
def saveFile(filename, personlist):
    content = open(filename, 'w')
    for obj in personlist:
        content.write(obj.familyname)
        content.write("\n")
        content.write(obj.name)
        content.write("\n")
        content.write(str(obj.number))
        content.write("\n")
        content.write(obj.address)
        content.write("\n")
    content.close()


# Söker efter ett namn i lista
def searchName(personlist, familyname, name):
    for obj in personlist:
        if obj.familyname.lower() == familyname.lower() and obj.name.lower() == name.lower():
            return obj
    return None


# Söker efter ett nummer i lista
def searchNumber(personlist, number):
    for obj in personlist:
        if int(obj.number) == number:
            return obj
    return None


# Lägger till en person i lista
def addPerson(personlist, person):
    personlist.append(person)


# Tar bort person från lista
def removePerson(personlist, familyname, name):
    obj = searchName(personlist, familyname, name)
    personlist.remove(obj)


# Sorterar lista efter bokstavordning på efternamnen
def sortList(personlist):
    personlist.sort(key=operator.attrgetter("familyname"), reverse=False)


# Ändrar nummer i lista
def changeNumber(personlist, familyname, name, newnumber):
    person = searchName(personlist, familyname, name)
    if person is None:
        print("Person kan inte hittas")
    else:
        person.changenumber(newnumber)


# Ändrar adress i lista
def changeAddress(personlist, familyname, name, newaddress):
    person = searchName(personlist, familyname, name)
    if person is None:
        print("Person kan inte hittas")
    else:
        person.changeaddress(newaddress)


# Skriver ut lista i sorterad ordning(Se sortList)
def printList(personlist):
    printstatement = ("%15s%15s%15s%32s") % ("Efternamn", "Förnamn", "Telefon", "Adress")
    print(printstatement)
    print("======================================================================================")
    sortList(personlist)
    for obj in personlist:
        print(obj)
    print()


# Meny med olika val
def menu(choice, personlist):
    try:
        choice = int(choice)
        if choice == 1:
            while True:
                familyname = input("Efternamn: ")
                name = input("Förnamn: ")
                print()
                person = searchName(personlist, familyname.strip(), name.strip())
                if person is None:
                    print("Personen finns inte i registret, försök igen!\n")
                else:
                    print(person.printsingleline())
                    break
        elif choice == 2:
            while True:
                number = input("Nummer: ")
                try:
                    number = int(number)
                    person = searchNumber(personlist, number)
                    if person is None:
                        print("Personen finns inte i registret, försök igen!\n")
                    else:
                        print(person.printsingleline())
                        break
                except:
                    print("Fel inmatning, skriv endast in siffror t.ex 278643: ")
        elif choice == 3:
            familyname = input("Efternamn: ")
            name = input("Förnamn: ")
            while True:
                number = input("Nummer: ")
                try:
                    number = int(number)
                    address = input("Adress: ")
                    newperson = Person(familyname.strip(), name.strip(), number, address.strip())
                    addPerson(personlist, newperson)
                    break
                except:
                    print("Fel inmatning, skriv endast in siffror t.ex 278643")
        elif choice == 4:
            familyname = input("Efternamn: ")
            name = input("Förnamn: ")
            removePerson(personlist, familyname.strip(), name.strip())
        elif choice == 5:
            familyname = input("Efternamn: ")
            name = input("Förnamn: ")
            while True:
                newnumber = input("Nytt nummer: ")
                try:
                    newnumber = int(newnumber)
                    changeNumber(personlist, familyname.strip(), name.strip(), newnumber)
                    break
                except:
                    print("Fel inmatning, skriv endast in siffror t.ex 27843: ")
        elif choice == 6:
            familyname = input("Efternamn: ")
            name = input("Förnamn: ")
            newaddress = input("Ny adress: ")
            changeAddress(personlist, familyname.strip(), name.strip(), newaddress.strip())
        elif choice == 7:
            printList(personlist)
        elif choice == 8:
            saveFile("register.txt", personlist)
            print("Hejdå!")
            os._exit(1)
        elif choice == 9:
            print("1: Söker efter ett namn i registret\n2: Söker efter ett nummer i registret\n"
                  "3: Lägg till en ny person i registret genom att mata in för- och efternamn, telefonnummer samt adress\n"
                  "4: Tar bort en person i registret genom att mata in för- och efternamn\n5: Ändrar en persons telefonnumer genom att söka på för- och efternamn, mata sedan in ett nytt telefonnummer\n"
                  "6: Samma som alternativ 5 fast med adressen istället\n7: Skriver ut alla personer i registret\n8: Avslutar telefonregistret och sparar sedan eventuella förändringar i telefonregistret\n")
        else:
            print("%s ligger inte i intervallet 1-9, välj igen!" % choice)
    except:
        print("%s är ingen siffra, välj mellan 1-9!" % choice)


# main
personlist = []
readFile("register.txt", personlist)
print("Välkommen till telefonregistret!")
while True:
    print("\nDet här kan du göra:")
    print("1.Sök efter namn\n2.Sök efter telefonnummer\n3.Lägg till nya uppgifter\n"
          "4.Ta bort uppgifter\n5.Ändra telefonnummer\n6.Ändra adress\n7.Skriv ut register\n8.Avsluta\n9.Hjälptext\n")
    choice = input("Välj: ")
    menu(choice, personlist)
