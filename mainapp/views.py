from django.shortcuts import render
from django.http import HttpResponse
import json
from . import connect as mysql
def home(request):
    return render(request,"index.html",{})

def about(request):
    return render(request,"about.html",{})

def contact(request):
    return render(request,"contact.html",{})

def save(request):
    username = request.POST['name']
    mail = request.POST['email']
    branch = request.POST['branch']
    password = request.POST['pwd']

    query = "insert into teacher(name,mail,branch,password) values('{0}','{1}','{2}','{3}')".format(username,mail,branch,password)
    mysql.executequery(query)
    return HttpResponse("done")
    
def login(request):
    mail=request.POST['mail']
    pass1=request.POST['pwd']

    query="select * from teacher where mail='{0}' and password='{1}'".format(mail,pass1)
    data = mysql.getRecords(query)
    if len(data)==0:
        return HttpResponse("<h1>ID or Password Invalid!</h1>")
    else:
        name=data[0][1]
        records = mysql.getrecords("select * from student")
        return render(request,'user.html',{"faculty":name})

def test(request):
    txt= request.GET['txt']
    return HttpResponse(txt + "Gits udaipur")

def search(request):
    txt=request.GET['txt']
    query = "select * from student where name LIKE '{0}%'".format(txt)
    data = mysql.getRecords(query)
    records = []
    for d in data:
        rec ={"roll":d[0],"name":d[1],"age":d[2],"marks":d[3]}
        records.append(rec)
    return HttpResponse(json.dumps(records))    


