from django.http import HttpResponse
from django.shortcuts import render

def car(request):
    return render(request,'index.html')

def sec(request):

    djtext = request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','off')
    capitalform = request.POST.get('capitalform', 'off')
    space_det=request.POST.get('space_det','off')
    char_counter=request.POST.get('char_counter','off')
    
    #to remove punctuations
    punctuations='''!()-[];.,<>!@#$%^&*:'"'''
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
    
    #to Create uppercase
    if capitalform == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
            
    #new_line remover
    if space_det == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        djtext = analyzed
    
    if char_counter == "on":
        a = 0
        for index,alpha in enumerate(djtext):
            if djtext[index].isalpha():
                a = a+1
    else:
        a=0
        
    if (removepunc != "on" and capitalform != "on" and char_counter != "on" and space_det != "on"):
        
        return render(request,'Error.html')

    elif (removepunc != "on" and capitalform != "on" and char_counter == "on" and space_det != "on"):
        analyzed = djtext
        print(analyzed)
          

    param={"one":analyzed, "two" : a }

    return render(request,'analyz.html',param)
