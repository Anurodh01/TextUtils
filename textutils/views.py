from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')


def analyze(request):
    mystring = request.POST.get('text')
    removepunc = request.POST.get('removepunc')
    charcount = request.POST.get('charcount')
    punctuations = '''!()-[]{};::'"\,<>,./?@#$%^&*_-~'''
    analyzed = ""
    if removepunc == 'on':
        for char in mystring:
            if char not in punctuations:
                analyzed = analyzed + char
    l = 0
    if charcount == 'on':
        for i in mystring:
            l = len(mystring)
    params = {'purpose': 'The Punctuations from the text has been removed',
              'another_purpose': 'The Total number of characters in text', 'character': l, 'analyzed': analyzed,'valid':'True'}
    if analyzed == "":
        params['purpose'] = ''
    if l == 0:
        params['another_purpose'] = ''
        params['character'] = ''
    return render(request, 'analyze2.html', params)
