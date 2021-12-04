from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .baza import *


# Create your views here.
class MainPage(View):
    def get(self, request):
        context = {}
        print("@@")
        print(request)
        return render(request, 'websity.html', context=context)

    def post(self, request):
        entered_login = request.POST.get("login")
        entered_passw = request.POST.get("password")
        users = autoriz(entered_login, entered_passw)
        if not users:
            context = {
                "message": "Введен неверный логин или пароль"
            }
            return render(request, 'websity.html', context=context)
        elif users[0].priority == "0":
            request.session["id_user"] = users[0].id
            request.session["priv_user"] = users[0].priority

            return HttpResponseRedirect('websityContract.html')
        else:
            request.session["id_user"] = users[0].id
            request.session["priv_user"] = users[0].priority
            return HttpResponseRedirect('websityContract1.html')


class Author(View):
    def get(self,request):
        context = {}
        return render(request, 'websityAuthor.html', context=context)

    def post(self, request):
        context = {}
        surname = request.POST.get("surname")
        name = request.POST.get("name")
        patronymic = request.POST.get("patronymic")
        address = request.POST.get("address")
        telephone = request.POST.get("telephone")
        passport = request.POST.get("passport")
        mail = request.POST.get("mail")

        if context:
            return render(request, "websityAuthor.html", context=context)
        else:
            add_author(surname, name, patronymic, address, telephone, passport, mail)
            return HttpResponseRedirect('websityFormalizeContract.html')


class Author1(View):
    def get(self,request):
        context = {}
        return render(request, 'websityAuthor1.html', context=context)

    def post(self, request):
        context = {}
        surname = request.POST.get("surname")
        name = request.POST.get("name")
        patronymic = request.POST.get("patronymic")
        address = request.POST.get("address")
        telephone = request.POST.get("telephone")
        passport = request.POST.get("passport")
        mail = request.POST.get("mail")

        if context:
            return render(request, "websityAuthor1.html", context=context)
        else:
            add_author(surname, name, patronymic, address, telephone, passport, mail)

            return render(request, "websityChangeContract.html", context=context)


class ChangeContract(View):
    def get(self,request):
        context = {}
        return render(request, 'websityChangeContract.html', context=context)

    def post(self, request):
        context = {}
        id = request.POST.get("id")
        contractDate = request.POST.get("contractDate")
        circulation = request.POST.get("circulation")
        format = request.POST.get("format")
        volume = request.POST.get("volume")
        dateExecution = request.POST.get("dateExecution")
        staff_id = request.POST.get("staff_id")
        publishing_id = request.POST.get("publishing_id")
        author_id = request.POST.get("author_id")


        update_contract(id,contractDate, circulation, format, volume, dateExecution, staff_id, publishing_id, author_id)
        contractss = get_contract()
        context = {
            'contractss': contractss
        }
        return render(request, 'websityContract.html', context=context)


class Contract(View):
    def get(self,request):
        contractss = get_contract()
        context = {
           'contractss': contractss
        }
        return render(request, 'websityContract.html', context=context)

    def post(self, request):
        context = {}
        id = request.POST.get("id")
        if id:
            idContract = get_contract_id(id)
            if request.POST.get("print"):
                context = {
                    'idContract': idContract,
                }
                return render(request, "websityPrint.html", context=context)
            elif request.POST.get("delete"):
                if id:
                    delete(id)
                contractss = get_contract()
                context = {
                    'contractss': contractss
                }
                return render(request, "websityContract.html", context=context)
            elif request.POST.get("update"):
                selectAuthor = get_author()
                selectPublishing = get_push()
                selectStaff = get_staff()
                context = {
                    'selectAuthor': selectAuthor,
                    'selectPublishing': selectPublishing,
                    'selectStaff': selectStaff,
                    'idContract': idContract,
                }
                return render(request, "websityChangeContract.html", context=context)
            elif request.POST.get("SaveUpdate"):
                id = request.POST.get("id")
                contractDate = request.POST.get("contractDate")
                circulation = request.POST.get("circulation")
                format = request.POST.get("format")
                volume = request.POST.get("volume")
                dateExecution = request.POST.get("dateExecution")
                staff_id = request.POST.get("staff_id")
                publishing_id = request.POST.get("publishing_id")
                author_id = request.POST.get("author_id")

                update_contract(id, contractDate, circulation, format, volume, dateExecution, staff_id, publishing_id,
                                author_id)
                contractss = get_contract()
                context = {
                    'contractss': contractss
                }
                return render(request, 'websityContract.html', context=context)
        if 'searchButton' in request.POST:
            searchs = request.POST.get("search")
            if searchs:
                contractss = search(searchs)
            else:
                contractss = get_contract()
            context = {
                'contractss': contractss
            }
            return render(request, "websityContract.html", context=context)
        elif 'searchButtonDate' in request.POST:
            searchDatee = request.POST.get("searchDate")
            if searchDate:
                contractss = searchDate(searchDatee)
            else:
                contractss = get_contract()

            context = {
                'contractss': contractss
            }
            return render(request, "websityContract.html", context=context)
        elif 'sort1' in request.POST:
            sort = request.POST.get("Sort")
            contractss = sort_id(sort)
            context = {
                'contractss': contractss
            }
            return render(request, "websityContract.html", context=context)
        elif 'onContract' in request.POST:
            contractss = get_contract()
            context = {
                'contractss': contractss
            }
            if request.session["priv_user"] == "0":
                return render(request, 'websityContract.html', context=context)
            else:
                return render(request, 'websityContract1.html', context=context)
        elif 'plus' in request.POST:
            id = request.POST.get("id")
            idContract = get_contract_id(id)

            context = {
                'idContract': idContract
            }
            return render(request, "websityAuthor1.html", context=context)
        elif 'back' in request.POST:
            id = request.POST.get("id")
            idContract = get_contract_id(id)
            context = {
                'idContract': idContract,
            }
            return render(request, "websityChangeContract.html", context=context)
        elif request.POST.get("addAuthor"):
            surname = request.POST.get("surname")
            name = request.POST.get("name")
            patronymic = request.POST.get("patronymic")
            address = request.POST.get("address")
            telephone = request.POST.get("telephone")
            passport = request.POST.get("passport")
            mail = request.POST.get("mail")

            add_author(surname, name, patronymic, address, telephone, passport, mail)

            id = request.POST.get("id")
            idContract = get_contract_id(id)
            selectAuthor = get_author()
            selectPublishing = get_push()
            selectStaff = get_staff()
            context = {
                'selectAuthor': selectAuthor,
                'selectPublishing': selectPublishing,
                'selectStaff': selectStaff,
                'idContract': idContract,
            }
            return render(request, "websityChangeContract.html", context=context)

        else:
            return HttpResponseRedirect('websityContract.html')


class Contract1(View):
    def get(self,request):
        contractss = get_contract()
        context = {
           'contractss': contractss
        }
        return render(request, 'websityContract1.html', context=context)

    def post(self, request):
        context = {}
        id = request.POST.get("id")
        if id:
            idContract = get_contract_id(id)
            if request.POST.get("print"):
                context = {
                    'idContract': idContract,
                }
                return render(request, "websityPrint.html", context=context)
        if 'searchButton' in request.POST:
            searchs = request.POST.get("search")
            if searchs:
                contractss = search(searchs)
            else:
                contractss = get_contract()
            context = {
                'contractss': contractss
            }
            return render(request, "websityContract1.html", context=context)
        elif 'sort1' in request.POST:
            sort = request.POST.get("Sort")
            contractss = sort_id(sort)
            context = {
                'contractss': contractss
            }
            return render(request, "websityContract1.html", context=context)
        elif 'onContract' in request.POST:
            contractss = get_contract()
            context = {
                'contractss': contractss
            }
            if request.session["priv_user"] == "0":
                return render(request, 'websityContract.html', context=context)
            else:
                return render(request, 'websityContract1.html', context=context)
        else:
            return HttpResponseRedirect('websityContract1.html')


class FormalizeContract(View):
    def get(self,request):
        selectAuthor = get_author()
        selectPublishing = get_push()
        selectStaff= get_staff()
        context = {
            'selectAuthor': selectAuthor,
            'selectPublishing': selectPublishing,
            'selectStaff': selectStaff
        }
        return render(request, 'websityFormalizeContract.html', context=context)

    def post(self, request):
        context = {}
        contractDate = request.POST.get("contractDate")
        circulation = request.POST.get("circulation")
        format = request.POST.get("format")
        volume = request.POST.get("volume")
        dateExecution = request.POST.get("dateExecution")
        staff_id = request.POST.get("staff_id")
        publishing_id = request.POST.get("publishing_id")
        author_id = request.POST.get("author_id")

        add_contract(contractDate, circulation, format, volume, dateExecution, staff_id, publishing_id,
                      author_id)

        return HttpResponseRedirect('websityContract.html')


class Print(View):
    def get(self,request):
        contractss = get_contract_id(id)
        context = {
            'contractss': contractss
        }
        return render(request, 'websityPrint.html', context=context)

    def post(self, request):
        contractss = get_contract()
        context = {
            'contractss': contractss
        }
        if request.session["priv_user"] == "0":
            return render(request, 'websityContract.html', context=context)
        else:
            return render(request, 'websityContract1.html', context=context)


class Print1(View):
    def get(self,request):
        context = {}
        return render(request, 'websityPrint1.html', context=context)


class Registration(View):
    def get(self,request):
        context = {}
        return render(request, 'websityReg.html', context=context)

    def post(self, request):
        context = {}
        surname = request.POST.get("surname")
        name = request.POST.get("name")
        patronymic = request.POST.get("patronymic")
        address = request.POST.get("address")
        telephone = request.POST.get("telephone")
        passport = request.POST.get("passport")
        mail = request.POST.get("email")
        loginReg = request.POST.get("loginReg")
        password = request.POST.get("passwordReg")
        loginSeach = loginSearch(loginReg)
        passwordSeach = passwordSearch(password)
        if loginSeach:
            context = {
                "message": "Логин уже занят"
            }
            return render(request, 'websityReg.html', context=context)
        elif passwordSeach:
            context = {
                "message": "Пароль уже занят"
            }
            return render(request, 'websityReg.html', context=context)
        else:
            add_staff(surname, name, patronymic, address, telephone, passport, mail, loginReg, password)

            return HttpResponseRedirect('websity.html')

        ''' if context:
                    return render(request, "websityReg.html", context=context)'''