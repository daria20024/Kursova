
from .models import *
from django.db.models import Q
import datetime

def get_contract():
    contracts = contract.objects.all()
    return contracts


def get_contract_id(id):
    contracts = contract.objects.get(id=id)
    return contracts


def get_author():
    authors = author.objects.all()
    return authors


def get_author_id(id):
    authors = author.objects.get(id=id)
    return authors


def get_push():
    publishings = publishing.objects.all()
    return publishings


def get_push_id(id):
    publishings = publishing.objects.get(id=id)
    return publishings


def get_staff():
    staffs = staff.objects.all()
    return staffs


def autoriz(login, passw):
    users = staff.objects.filter(login=login, password=passw)
    return users


def search(word):
    '''searchs = contract.objects.filter(Q(id=word) | Q(contractDate=word) | Q(circulation=word) | Q(format=word) |
                                    Q(volume=word) | Q(dateExecution=word) | Q(staf=word) | Q(publish=word) |
                isinstance()                    Q(auth=word))'''
    try:
        word = int(word)
        searchs = contract.objects.filter(Q(id=word) | Q(circulation=word) | Q(volume=word))
        '''except ValueError:
        word = datetime.datetime.strptime(word, '%b %d %Y %I:%M%p')
        print(word.date())
        searchs = contract.objects.filter(Q(contractDate=word.date()) | Q(dateExecution=word.date()))'''
    except BaseException:
        searchs = contract.objects.filter(Q(format=word))

    '''if isinstance(int(word), int):word.date()
        searchs = contract.objects.filter(Q(id=int(word))  | Q(circulation=word) | Q(format=word))
    elif isinstance(word, str):'''

    return searchs


def add_contract(contractDate, circulation, format, volume, dateExecution, staf, publish, auth):

    a_contract = contract(contractDate=contractDate,
                        circulation=circulation,
                        format=format,
                        volume=volume,
                        dateExecution=dateExecution,
                        staff_id = staff.objects.get(id=staf),
                        publishing_id = publishing.objects.get(id=publish),
                        author_id = author.objects.get(id=auth))
    a_contract.save()


def add_author(surname, name, patronymic, address, telephone, passport, mail):

    a_author = author(surname=surname,
                        name=name,
                        patronymic=patronymic,
                        address=address,
                        telephone = telephone,
                        passport = passport,
                        mail = mail)
    a_author.save()


def add_staff(surname, name, patronymic, address, telephone, passport, mail, loginReg, password):

    a_staff = staff(surname=surname,
                        name=name,
                        patronymic=patronymic,
                        address=address,
                        telephone = telephone,
                        passport = passport,
                        mail = mail,
                        login = loginReg,
                        password = password)
    a_staff.save()


def update_contract(id, contractDate, circulation, format, volume, dateExecution, staff_id, publishing_id, author_id):
    u_contract= contract.objects.get(id=id)
    u_contract.contractDate=contractDate
    u_contract.circulation=circulation
    u_contract.format=format
    u_contract.volume=volume
    u_contract.dateExecution=dateExecution
    u_contract.staff_id=staff.objects.get(id=staff_id)
    u_contract.publishing_id=publishing.objects.get(id=publishing_id)
    u_contract.author_id = author.objects.get(id=author_id)
    u_contract.save()


def delete(id):
    person = contract.objects.get(id=id)
    person.delete()

