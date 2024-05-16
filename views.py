from django.shortcuts import render,HttpResponse
from .models import Maintenance
from .models import Workers
from .models import finance
from .models import project
from .models import type



#create your views here
def index(request):
    return render(request,'index.html')

def home(request):
    return render (request,'Home.html')

def login(request):
    return render (request,'login.html')


def maintainancelist(request):
    listdata=Maintenance.objects.all()
    showlist={
	'list':listdata
	}
    return render (request,'maintainancelist.html',showlist)

def workerslist(request):
    wlistdata=Workers.objects.all()
    showlist={
	'workerslist':wlistdata
	}
    return render (request,'workerslist.html',showlist)

def financelist(request):
    flistdata=finance.objects.all()
    showlist={
	'financelist':flistdata
	}
    return render (request,'financelist.html',showlist)

def projectlist(request):
    plistdata=project.objects.all()
    showlist={
    'projectlist':plistdata
    }
    return render (request,'projectlist.html',showlist)

def typelist(request):
   tlistdata=type.objects.all()
   showlist={
   'typelist':tlistdata
   }
   return render (request,'typelist.html',showlist)

