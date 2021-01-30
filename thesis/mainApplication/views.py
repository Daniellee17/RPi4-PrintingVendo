from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def mainPage(response):

    if response.POST.get('action') == 'setup':

        print(" ")
        print("--------------------------- GrowSmart Initializing ----------------------------")
        print(" ")
        print(" ")

        json = {
        'modeNumber' : "1"
        }
        return JsonResponse(json)

    if response.POST.get('action') == 'onFan':

        print(" ")
        print("~Air Circulation System Activated~")
        print(" ")


    return render(response, 'main.html')
