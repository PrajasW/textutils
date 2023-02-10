# made by prajas
from django.http import HttpResponse
from django.shortcuts import render
# code for video 6
# def index(request):
#     return HttpResponse("<h1>Hello</h1>")
#
# def about(request):
#     return HttpResponse("about")
#
# def komm(request):
#     return HttpResponse('''
#     <a href= "https://www.youtube.com/watch?v=_N66Hud_Tq4&list=RD_N66Hud_Tq4&start_radio=1">komm susser todd</a>
#     <br>
#     <a href= "https://www.youtube.com/watch?v=upLNuwE2uKs&list=RD_N66Hud_Tq4&index=3">Duet</a>
#     <br>
#     <a href= "">komm susser todd</a>
#     <a href= "https://www.youtube.com/watch?v=_N66Hud_Tq4&list=RD_N66Hud_Tq4&start_radio=1">komm susser todd</a>
#     <a href= "https://www.youtube.com/watch?v=_N66Hud_Tq4&list=RD_N66Hud_Tq4&start_radio=1">komm susser todd</a>
#
#     ''')

# lec 07
# def index(request):
#     return HttpResponse(
#         '''
#         <h1> home </h1>
#         <br>
#         <a href="/removepunc"><button type="button">remove punc</button></a>
#         <a href="/capfirst"><button type="button">capfirst</button></a>
#         <a href="/newlineremove"><button type="button">new line remove</button></a>
#         <a href="/spaceremove"><button type="button">space remove</button></a>
#         <a href="/charcount"><button type="button">char count</button></a>
#         '''
#     )
#
# def removepunc(request):
#     return HttpResponse('''
#     <h1> remove punctuations </h1>
#     <a href="/"><button type="button">Home</button></a>
#     ''')
#
# def capfirst(request):
#     return HttpResponse('''
#     <h1> cap first </h1>
#     <a href="/"><button type="button">Home</button></a>
#     ''')
# def newlineremove(request):
#     return HttpResponse('''
#     <h1> new line remove </h1>
#     <a href="/"><button type="button">Home</button></a>
#     ''')
#
# def spaceremove(request):
#     return HttpResponse('''
#     <h1> remove punctuations </h1>
#     <a href="/"><button type="button">Home</button></a>
#     ''')
# def charcount(request):
#     return HttpResponse('''
#     <h1> remove punctuations </h1>
#     <a href="/"><button type="button">Home</button></a>
#     ''')def index(request):
#     return HttpResponse(
#         '''
#         <h1> home </h1>
#         <br>
#         <a href="/removepunc"><button type="button">remove punc</button></a>
#         <a href="/capfirst"><button type="button">capfirst</button></a>
#         <a href="/newlineremove"><button type="button">new line remove</button></a>
#         <a href="/spaceremove"><button type="button">space remove</button></a>
#         <a href="/charcount"><button type="button">char count</button></a>
#         '''
#     )

#lec 08

def index(request):
    return render(request,'home.html')

# def removepunc(request):
#     #get the text from home (textbox name="text")
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     #analyse the text
#
#     parmas = {'function':'remove punctuation'}
#     return render(request,'index.html',parmas)
#
# def capfirst(request):
#     parmas = {'function':'capitilize first'}
#     return render(request,'index.html',parmas)
# def newlineremove(request):
#     parmas = {'function':'new line remove'}
#     return render(request,'index.html',parmas)
#
# def spaceremove(request):
#     parmas = {'function':'remove space'}
#     return render(request,'index.html',parmas)
# def charcount(request):
#     parmas = {'function':'cont characters'}
#     return render(request,'index.html',parmas)

def analyze(request):
    intext = request.POST.get('text', 'Error in fetching')
    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    # capfirst = request.GET.get('capfirst','off')
    # newlineremove = request.GET.get('newlineremove','off')
    # spaceremove = request.GET.get('spaceremove','off')
    # charcount = request.GET.get('charcount','off')
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
    small = "abcdefghijklmnopqrstuvwxyz"
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if(fullcaps == 'on'):
        fullcaps.upper()
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