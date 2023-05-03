from django.http import HttpResponse # it is not call any page
from django.shortcuts import render # it can call any page like htmlpage 


#add the html files
def homePage(request):
    # return render(request,'index.html') # render call the html page

    # we pass the data in html page
    # data={
    #     'title':'Home Page',
    #     'pargraph':"this is dynamic paragraph, it comes from view.py files",
    #     'clist':['c','c++','python','java'],
    #     'student_details':[
    #         {'name':'sushil','phone':2948750384},
    #         {'name':'sahil','phone':123847543}
    #         ],
    #     'number':[1,2,5,6,35,4]
    # }
    # return render(request,'index.html',data)
    
    return render(request,'calcuator.html')

'''
# we add html page
def aboutUs(request):
    # we also use html tags 
    return HttpResponse('<b>welcome to my new project</b>')


def course(request):
    # we also use html tags 
    return HttpResponse('<b>welcome to my new project course</b>')

def courseDetails(request,courseid):
    # we also use html tags 
    return HttpResponse(f'<b>welcome to my new project courseDetails</b>{courseid}')
 '''