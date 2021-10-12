from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.
class MainPage(View):
    def get(self,request):
        context = {}
        return render(request, 'websity.html', context=context)


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
        context = {}
        return render(request, 'websityContract.html', context=context)


class FormalizeContract(View):
    def get(self,request):
        context = {}
        return render(request, 'websityFormalizeContract.html', context=context)


class Print(View):
    def get(self,request):
        context = {}
        return render(request, 'websityPrint.html', context=context)


class Registration(View):
    def get(self,request):
        context = {}
        return render(request, 'websityReg.html', context=context)