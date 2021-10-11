from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.
class MainPage(View):
    def get(self,request):
        context = {}
        return render(request, 'websity.html', context=context)