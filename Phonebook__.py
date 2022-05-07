import json as j

class Phonebook:
    def __init__(self, first, last, phone, town, exact_place):
        self.first = first
        self.last = last
        self.phone = phone
        self.town = town
        self.exact_place = exact_place
        self.email = f'{first}_{last}.{exact_place}@{town}.com'
        self.user_number = Phonebook.count_users(4)
        with open('phonebook.json', 'a+') as o:
            dict = {'first name': first, 'last name': last, 'town': town,
                    'exact_place': exact_place, 'email': self.email,
                    'phone number': phone, 'user number': self.user_number}
            list = []
            try:
                with open('phonebook.json', 'r') as o:
                    lo = j.load(o)
                    lo.append(dict)
                with open('phonebook.json', 'w') as o:
                    j.dump(lo, o, ensure_ascii=False)
            except:
                with open('phonebook.json', 'w') as o:
                    list.append(dict)
                    j.dump(list, o, ensure_ascii=False)

    def count_users(self):
        try:
            with open('phonebook.json', 'r') as o:
                number = j.load(o)
                user = 0
            user = len(number) + 1
            return user
        except:
            return 0

    number_of_users = count_users(0)


    def __str__(self):
        self_dict = {'first name': self.first, 'last name': self.last, 'town': self.town,
               'exact place': self.exact_place, 'email': self.email,
               'phone number': self.phone, 'user number': self.user_number}
        return str(self_dict)

def search_contact(date, place):
    with open('phonebook.json', 'r') as o:
        l1 = []
        list = j.load(o)
        for i in list:
            if i[place] == date:
               l1.append(i)
    return l1

def delete_contact(num):
    with open('phonebook.json', 'r') as o:
        delete = j.load(o)
        delete.remove(num)
    with open('phonebook.json', 'w') as o:
        j.dump(delete, o)

def change_contact(contact, town, change):
    with open('phone_book.json', 'r') as o:
        changer = j.load(o)
        for i in changer:
            if i == contact:
                var = i
                i[town] = change
                with open('phone_book.json', 'w') as o:
                    j.dump(changer, o)


def main():
    phonenum = 1234567890
    while phonenum != 0:
        try:
            print('')
            phonenum = int(input('''                                To search contact input 1
                                 To create contact input 2 
                                 To delete contact input 3
                                 To change contact input 4
                                 To finish input 0 
                                 to see number of contacts input 5
                                 Input here: '''))
        except ValueError:
            print('invalid number')
        if phonenum == 1:
            searcher = input('''What parameter do you want to search with? 
                           For example: first name:... ''')
            search_info = input('''What information does your contact have? 
                                   For example: Vasya: ''')
            try:
                search_info = int(search_info)
            except:
                pass
            try:
                print(f" Here is your contact(s){search_contact(search_info, searcher)}")
            except:
                print('Sorry, invalid contact information. Enter correct information')

        if phonenum == 2:
            try:
                first = input('Input a first name of contact: ')
                last = input('Input a last name of contact: ')
                town = input('Input city where your contact live: ')
                exact = input('Input an address where contact live: ')
                phone = int(input('Input a phone number of contact: '))
                contact = Phonebook(first, last, town, exact, phone)
            except ValueError:
                print('Invalid phone number')
                phonenum = 2
        if phonenum == 3:
            try:
                deleter = input('Input a contact which would you like to delete: ')
                delete = j.loads(deleter)
                delete_contact(delete)
            except ValueError:
                print('invalid contact')
        if phonenum == 4:
            changer = input('Input a contact which would you like to change: ')
            changer1 = j.loads(changer)
            changer2 = input(' What information do you want to change in the contact? For example: phone: ')
            changer3 = input('What information should your contact have? For example: town: ')
            try:
                change_contact(changer1, changer2, changer3)
            except ValueError:
                print('Invalid information')
        if phonenum == 5:
            print(Phonebook.number_of_users)

main()
