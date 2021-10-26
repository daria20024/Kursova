from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .baza import *


# Create your views here.
class MainPage(View):
    def get(self, request):
        context = {}
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


class ChangeContract(View):
    def get(self,request):
        context = {}
        return render(request, 'websityChangeContract.html', context=context)


class Contract(View):
    def get(self,request):
        contractss = get_contract()
        context = {
           'contractss': contractss
        }
        return render(request, 'websityContract.html', context=context)


class Contract1(View):
    def get(self,request):
        contractss = get_contract()
        context = {
           'contractss': contractss
        }
        return render(request, 'websityContract1.html', context=context)


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



        if context:
            return render(request, "websityFormalizeContract.html", context=context)
        else:
            add_contract(contractDate, circulation, format, volume, dateExecution, staff_id, publishing_id,
                      author_id)

            return HttpResponseRedirect('websityContract.html')


class Print(View):
    def get(self,request):
        context = {}
        return render(request, 'websityPrint.html', context=context)


class Print1(View):
    def get(self,request):
        context = {}
        return render(request, 'websityPrint1.html', context=context)


class Registration(View):
    def get(self,request):
        context = {}
        return render(request, 'websityReg.html', context=context)