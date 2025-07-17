from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='signin') 
def shedule_view(request):
    user = request.user
    user_department = user.department
    user_batch = user.batch


    DAYS = [
        'sunday',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
    ]

    if user_department and user_batch:
        shedule = Shedule.objects.filter(department=user_department, batch=user_batch)
    else:
        shedule = Routeen.objects.none()


    return render(request, 'shedule.html', {
        'user': user,
        'days': DAYS,
        'shedule': shedule
    })