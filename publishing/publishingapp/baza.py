
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


def sort_id(sort):
    if sort == 'ID':
        users = contract.objects.order_by('id')
    elif sort == 'contractDate':
        users = contract.objects.order_by('contractDate')
    elif sort == 'circulation':
        users = contract.objects.order_by('circulation')
    elif sort == 'format':
        users = contract.objects.order_by('format')
    elif sort == 'volume':
        users = contract.objects.order_by('volume')
    elif sort == 'dateExecution':
        users = contract.objects.order_by('dateExecution')
    elif sort == 'staff_id':
        users = contract.objects.order_by('staff_id')
    elif sort == 'publishing_id':
        users = contract.objects.order_by('publishing_id')
    elif sort == 'author_id':
        users = contract.objects.order_by('author_id')
    else:
        users = contract.objects.order_by('id')
    return users


def search(word):
    try:
        word = int(word)
        searchs = contract.objects.filter(Q(id=word) | Q(circulation=word) | Q(volume=word))
    except BaseException:
        contracts = contract.objects.all()
        wordA = 0
        wordP = 0
        wordS = 0
        for c in contracts:
            if c.publishing_id.title == word:
                wordP = c.publishing_id
            if c.staff_id.surname == word:
                wordS = c.staff_id
            if c.author_id.surname == word:
                wordA = c.author_id
        searchs = contract.objects.filter(Q(format=word)| Q(publishing_id=wordP) | Q(staff_id=wordS) | Q(author_id=wordA))

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

