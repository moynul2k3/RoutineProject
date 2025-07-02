from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def home(request):
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


