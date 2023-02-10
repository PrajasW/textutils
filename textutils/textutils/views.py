# made by prajas
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'home.html')

def analyze(request):
    intext = request.POST.get('text', 'Error in fetching')
    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    print(intext)
    analyzed = intext

    #removing punctuations if checked
    punctuations = '''!(){}[];:'"/,<>.\?!@##$%^&*~`-_=+'''
    if(removepunc == 'on'):
        analyzed = ''
        for char in intext:
            if(char not in punctuations):
                analyzed = analyzed + char
    #capitlizing all
    if(fullcaps == 'on'):
        analyzed = analyzed.upper()
    #newline remover
    if(newlineremover == 'on'):
        temp = analyzed
        analyzed = ""
        for char in temp:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char
    #space remover
    if(spaceremover == 'on'):
        temp = analyzed
        analyzed = ''
        for char in temp:
            if char != ' ':
                analyzed = analyzed + char
    #extra space remover
    if(extraspaceremover == 'on'):
        temp = analyzed
        analyzed = ''
        for i in range(0, len(temp)):
            if not ((temp[i] == ' ') and (temp[i+1] == ' ')):
                analyzed = analyzed + temp[i]
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    count = 0
    for c in analyzed:
        if c in letters:
            count = count+1
    #displaying stuff
    params = {
        'analyzetext': analyzed,
        'charcount': count,
    }

    return render(request,'analyze.html',params)