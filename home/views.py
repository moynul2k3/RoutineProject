from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from my_routine.models import *
import datetime
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user = request.user
        user_department = user.department
        user_batch = user.batch
        today_name = datetime.datetime.today().strftime('%A')
        today = today_name.lower()

        if user_department and user_batch:
            shedule = Shedule.objects.filter(department=user_department, batch=user_batch, day__iexact=today).first()
        else:
            shedule = Routeen.objects.none()

        return render(request, 'home.html',{
            'today_name': today_name,
            'shedule': shedule,
        })
    return render(request, 'home.html')

@login_required(login_url='signin') 
def routeenList(request):
    user = request.user
    # Assuming user has 'department' and 'batch' as ForeignKeys
    user_department = user.department
    user_batch = user.batch

    if user_department and user_batch:
        routeens = Routeen.objects.filter(department=user_department, batch=user_batch)
    else:
        routeens = Routeen.objects.none()
    return render(request, 'routeenList.html', {'routeens': routeens})



@login_required(login_url='signin') 
def routeen(request, pk):
    routeen = Routeen.objects.filter(pk=pk).first()
    return render(request, 'routeen.html', {'routeen': routeen})


