from django.shortcuts import render, redirect
from home.models import *
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import get_user_model
UserAccount = get_user_model() # adjust import as needed
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

def sign_in(request):
    if request.method == 'POST':
        identifier = request.POST.get('email')  # this field holds email or REG_no
        password = request.POST.get('password')

        # Try to authenticate by email
        user = authenticate(request, email=identifier, password=password)

        # If not authenticated by email, try by REG_no
        if user is None:
            user = authenticate(request, REG_no=identifier, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('routeenlist')  # change to your landing page
        else:
            messages.error(request, 'Invalid credentials, please try again.')
    return render(request, 'signin.html') 




def sign_up(request):
    departments = Department.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        REG_no = request.POST.get('reg')
        department_id = request.POST.get('department')
        batch_id = request.POST.get('batch')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        print('department_id: ', department_id)
        print('batch_id: ', batch_id)

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'sign_up.html', {'departments': departments})

        try:
            # Optional: You can also validate if department and batch exist
            department = Department.objects.get(id=department_id)
            batch = Batch.objects.get(id=batch_id)

            user = UserAccount.objects.create_user(
                email=email,
                REG_no=REG_no,
                password=password,
                name=name,
                department = department,
                batch = batch
            )

            messages.success(request, 'Account created successfully.')
            user.backend = 'core.backends.AuthBackend'
            login(request, user)
            return redirect('routeenlist')
        except IntegrityError:
            messages.error(request, 'Email or REG_no already exists.')
        except Department.DoesNotExist:
            messages.error(request, 'Invalid department selected.')
        except Batch.DoesNotExist:
            messages.error(request, 'Invalid batch selected.')

    return render(request, 'sign_up.html', {'departments': departments})


def get_batches(request, department_id):
    batches = Batch.objects.filter(department_id=department_id).order_by('-name')
    batch_data = [{'id': b.id, 'name': b.name} for b in batches]
    return JsonResponse({'batches': batch_data})


def logout_view(request):
    logout(request)
    return redirect('/')