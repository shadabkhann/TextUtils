
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
from pyparsing import punc8bit


def index(request):
    return render(request, 'index.html')


def analyze(request):

    djtext = request.POST.get('text', 'defualt')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed+char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == "" and djtext[index + 1] == ""):
                analyzed = analyzed+char
        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select the operator")

    return render(request, 'analyze.html', params)
