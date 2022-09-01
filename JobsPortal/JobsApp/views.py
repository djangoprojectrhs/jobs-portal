from django.shortcuts import render
from JobsApp.models import*

# Create your views here.
def index(request):
    return render(request, 'JobsApp/index.html')

def hydjobsinfo(request):
    jobs_list=hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request, 'JobsApp/hyd.html' , context=my_dict)

def bangalorejobsinfo(request):
    jobs_lst=bangalorejobs.objects.all()
    my_dict={'jobs_lst':jobs_lst}
    return render(request, 'JobsApp/bangalore.html' , context=my_dict)
