# This is a file created by -  Govind
from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("About Govind")    

def analyze(request):
    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    removenewline = request.POST.get("removenewline",'off')
    removeextraspace = request.POST.get('removeextraspace','off')
    charactercounter = request.POST.get('charactercounter','off')

    #Code for Removing Puntuations
    if removepunc == 'on':
        analyzed = ''
        punchuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punchuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punchuations','analyzed_text':analyzed}
        djtext = analyzed
        
        

    #Code to Convert the caracters in uppercase
    if(fullcaps=='on'):
        analyzed = ''
        for char in djtext:
            analyzed = djtext.upper() 

        params = {'purpose':'Convert to Uppercase','analyzed_text':analyzed}
        djtext = analyzed
           

    #Code for removing new Lines
    if(removenewline == 'on'):
        analyzed=''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
                
                params = {'purpose':'Remove new Line','analyzed_text':analyzed}
                djtext = analyzed

    #Code for Removing extra spaces
    if(removeextraspace == 'on'):
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
                
        params = {'purpose':'Remove extra space','analyzed_text':analyzed}
        djtext = analyzed


    # Code for Counting to characters in the String except space
    if(charactercounter == 'on'):
        count = 0
        #Counts each character except space.
        for i in range(0, len(djtext)):
            #This Line removes also the space
            # if(djtext[i] != ' '): 
            count = count + 1
    
       
        params = {'purpose':'Charcter Counter','analyzed_text':count}
        
    if(removepunc != 'on' and fullcaps != 'on' and charactercounter != 'on' and removenewline!= 'on' and removeextraspace!='on'):
        return HttpResponse("Please select atleast one Analyzer! Try Again")    
    
        
    return render(request,'analyze.html',params) 