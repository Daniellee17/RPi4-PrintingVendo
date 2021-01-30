#   git config --global user.email "danielleespiritu17@gmail.com"
#   git config --global user.name "Daniellee17"

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import os, sys, subprocess
import time, pprint, cups

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

        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, 'print.pdf'])

        conn = cups.Connection()
        printers = conn.getPrinters ()
        pprint.pprint(printers)
        print()

        printer = conn.getDefault()
        print("Default1:", printer)

        if printer == None:
            printer = list(printers.keys())[0]
            print("Default2:", printer)

        myfile = "./test.txt"
        pid = conn.printFile(printer, myfile, "test", {})
        while conn.getJobs().get(pid, None) is not None:
            time.sleep(1)
        #done



    return render(response, 'main.html')
