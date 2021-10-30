
from .models import *


def get_contract():
    contracts = contract.objects.all()
    return contracts


def get_author():
    authors = author.objects.all()
    return authors


def get_push():
    publishings = publishing.objects.all()
    return publishings

def get_staff():
    staffs = staff.objects.all()
    return staffs


def autoriz(login, passw):
    users = staff.objects.filter(login=login, password=passw)
    return users


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