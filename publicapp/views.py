from django.shortcuts import render,redirect
from publicapp.models import Contractor,Companies,Job
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def Contractorlist(request):
    c=Contractor.objects.all()
    return render(request,'contractorlist.html',{'c':c})
def Companieslist(request):
    c=Companies.objects.all()
    return render(request,'companieslist.html',{'c':c})

def Contractorlistdelete(request,id):
    c=Contractor.objects.get(id=id)
    c.delete()
    return redirect('/contractor')
def Companieslistdelete(request,id):
    c=Companies.objects.get(id=id)
    c.delete()
    return redirect('/company')

def Contractorlistdetail(request,id):
    c=Contractor.objects.get(id=id)
    return render(request,'contractorlistdetail.html',{'c':c})
def Companieslistdetail(request,id):
    c=Companies.objects.get(id=id)
    return render(request,'companieslistdetail.html',{'c':c})

def Contractorlistupdate(request,id):
    c=Contractor.objects.get(id=id)
    if request.method=='POST':
        c=Contractor.objects.get(id=id)
        
        cname=request.POST['name']
        ccity=request.POST['city']
        ccode=request.POST['zip_code']
        c.name=cname
        c.city=ccity
        c.zip_code=ccode
        c.save()
        return redirect('/contractor')
    return render(request,'contractorlistupdate.html',{'c':c})
def Companieslistupdate(request,id):
    c=Companies.objects.get(id=id)
    if request.method=='POST':
        c=Companies.objects.get(id=id)
        
        cname=request.POST['name']
        ccity=request.POST['city']
        ccode=request.POST['zip_code']
        c.name=cname
        c.city=ccity
        c.zip_code=ccode
        c.save()
        return redirect('/company')
    return render(request,'companieslistupdate.html',{'c':c})




def Contractorlistcreate(request):
    if request.method=='POST':
        cid=request.POST['id']
        cname=request.POST['name']
        ccity=request.POST['city']
        ccode=request.POST['zip_code']
        Contractor.objects.create(id=cid,name=cname,city=ccity,zip_code=ccode)
        return redirect('/contractor')
    return render(request,'contractorlistcreate.html')

def Companieslistcreate(request):
    if request.method=='POST':
        cid=request.POST['id']
        cname=request.POST['name']
        ccity=request.POST['city']
        ccode=request.POST['zip_code']
        Companies.objects.create(id=cid,name=cname,city=ccity,zip_code=ccode)
        return redirect('/company')
    return render(request,'companieslistcreate.html')


def Joblist(request):
    j=Job.objects.all()
    return render(request,'joblist.html',{'j':j})


def Jobcreate(request):
    c1=Contractor.objects.all()
    c2=Companies.objects.all()
    if request.method=='POST':
        jid=request.POST['id']
        jtitle=request.POST['title']
        jprice=request.POST['price']
        jcompany=request.POST['company']
        jcontractor=request.POST['contractor']
        jdate=request.POST['date']
        jtime=request.POST['time']

        Job.objects.create(id=jid,title=jtitle,price=jprice,company=jcompany,contractor=jcontractor,date=jdate,time=jtime)
        return redirect('/')


    return render(request,'jobcreate.html',{'c1':c1,'c2':c2})

def Jobdelete(request,id):
    j=Job.objects.get(id=id)
    j.delete()
    return redirect('/')
def Jobdetail(request,id):
    j=Job.objects.get(id=id)
    return render(request,'jobdetail.html',{'j':j})

def Jobupdate(request,id):
    j=Job.objects.get(id=id)
    c1=Contractor.objects.all()
    c2=Companies.objects.all()
    if request.method=='POST':
        j=Job.objects.get(id=id)
        jtitle=request.POST['title']
        jprice=request.POST['price']
        jcompany=request.POST['company']
        jcontractor=request.POST['contractor']
        jdate=request.POST['date']
        jtime=request.POST['time']
        j.title=jtitle
        j.price=jprice
        j.company=jcompany
        j.contractor=jcontractor
        j.date=jdate
        j.time=jtime
        j.save()
        return redirect('/')
    return render(request,'jobupdate.html',{'j':j,'c1':c1,'c2':c2})

def loginview(request):
    if request.method=='POST':
        user = request.POST["username"]
        password = request.POST["password"]
        data = authenticate(username=user, password=password)
        if data != None:
            login(request, data)
        return redirect('/company')
    return render(request,'login.html')

def logoutview(request):
    logout(request)
    return redirect("/")



    