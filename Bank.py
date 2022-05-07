import datetime as date
from functools import wraps


def time_logger(func):
    import time
    wraps(func)
    def timee(*args, **kwargs):
        time1 = time.time()
        result = func(*args, **kwargs)
        time2 = time.time()
        timer = f'Time of this function is {time2 - time1} seconds'
        with open("logs.txt", 'a') as logs:
            logs.write(timer)
            logs.write(' name is ')
            logs.write(func.__name__)
            logs.write('\n')
        return result
    return timee


def inform_logger(func):
    def timee(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('logs2.txt', 'a') as logs:
            logs.write(f' action --- {func.__name__}')
            name = func.__name__
        if name == 'çredit_to_card':
             with open('logg.txt', 'a') as logs:
                logs.write(f' number -- {BankAccount.number}  ')
                logs.write(f'money -- {BankAccount.money}\n')
        if name == 'withdraw':
            with open('logg.txt', 'a') as log:
                log.write(f' pin -- {BankAccount.pin}  ')
                log.write(f'money -- {BankAccount.money}\n')
        else:
            with open('logg.txt', 'a') as log:
                log.write(f' cvv -- {BankAccount.cvv}, date -- {BankAccount.date}, reciver -- {BankAccount.an_ac}\n')
        return result

    return timee


class BankAcount:
    nums = []
    @staticmethod
    def date():
        a = str(date.datetime.now()).split()
        a = a[0]
        a = a.split('-')
        a = f'{a[1]}/{a[2]}'
        return a
    def __init__(self,name, pin, number, cvv, money=0):
        for i in BankAcount.nums:
            if i == number:
                print('This number is already exists')
                return
        self.name = name
        self.__pin = pin
        self.number = number
        self.__cvv = cvv
        self._date = BankAcount.date()
        self.__money = money
        BankAcount.nums.append(number)
    @inform_logger
    def print_money(self, pin):
        if self.__pin == pin:
            return self.__money
    @inform_logger
    @time_logger
    def credit_to_card(self, number, money):
        if number == None:
            return number
        if self.number == number:
            self.__money += money
            return 'Transacttion complited'
        else:
            return 'Error'

    @inform_logger
    @time_logger
    def withdraw(self, pin, money):
        if self.__pin == pin:
            self.__money += money
            return 'Transacttion complited'
        else:
            return 'Error'

    @inform_logger
    @time_logger
    def trans_to_card(self, another_acount, cvv, date, money):
        if self.__cvv == cvv and self._date == date:
            self.__money += money
            another_acount.__money -= money
            return 'Transacttion complited'
        else:
            return 'Error'
class BankAccount:
    date = 0
    numer = 0
    cvv = 0
    pin = 0
    an_ac = 0
    money = 0
    @staticmethod
    def print_money(account):
        try:
            pin = int(input('input a pin: '))
        except:
            return 'it is not number'
        return BankAcount.print_money(account, pin)
    @staticmethod
    @time_logger
    def credit_to_card(account):
        try:
            number = int(input('input a number: '))
        except:
            return 'it is not number'
        try:
            money = int(input('number of money: '))
        except:
            return 'it is not number'
        BankAccount.number = number
        BankAccount.money = money
        return account.credit_to_card(number, money)

    @staticmethod
    @time_logger
    def withdraw(account):
        try:
            pin = int(input('input a pin: '))
        except:
            return 'it is not number'
        try:
            money = int(input('number of money: '))
            money = money * -1
        except:
            return 'it is not number'
        BankAccount.pin = pin
        BankAccount.money = money * -1
        return account.withdraw(pin, money)

    @staticmethod
    @time_logger
    def trans_to_card(account, another_ack):
        try:
            date = input('Date: ')
            cvv = int(input('CVV: '))
        except:
            return 'It is not number'
        try:
            money = int(input('Number of money: '))
            money = money * -1
        except:
            return 'It is not number'
        BankAccount.money = money * -1
        BankAccount.cvv = cvv
        BankAccount.date = date
        BankAccount.an_ac = another_ack.ame
        return account.trans_to_card(another_ack, cvv, date, money)


def main(borya_johnsonuk, vova_zelenskiy):
    a = 0
    while a != 235.5:
        try:
            a = int(input('''
            What do you want to do? 
            1 -- Credit to card
            2 -- Withdraw
            3 -- Trans out of card
            4 -- Check your balance
            5 -- Finish
            Input here: '''))
        except:
            print('It is not a number')
        if a == 1:
            print(BankAccount.credit_to_card(borya_johnsonuk))
            print('Try again')
        if a == 2:
            print(BankAccount.withdraw(borya_johnsonuk))
        if a == 3:
            print(BankAccount.trans_to_card(borya_johnsonuk, vova_zelenskiy))
        if a == 4:
            print(BankAccount.print_money(borya_johnsonuk))
        if a == 5:
            return

borya_johnsonuk = BankAcount('Borya', 1986, 845629462056274, 923)
vova_zelenskiy = BankAcount('Vovka', 2008, 444113475254135, 217)
main(borya_johnsonuk, vova_zelenskiy)