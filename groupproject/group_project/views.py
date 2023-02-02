from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *


# Create your views here.
def index(request):
    employees = get_employees(request)
    context = {
        "employees" : employees,
    }
    for emp in employees:
        print(emp.first_name)
        
    return render(request, 'index.html',context)

# login page
def login_page(request):
    return render(request,'login.html')

# login method
def login(request):
    error = members.objects.sigin_validator(request.POST)
    if len(error) > 0:
        print("***** 2 ")
        for key, value in error.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/login_page')
    else:
        userId =  Login(request)
        print(userId)
        if userId != None :
            print("333")
            request.session['userid'] = userId
            user = members.objects.get(id =request.session['userid'] )
            if user.user_level == 'admin' :
                print("444")
                return redirect('/dashboard_page')
            else:
                return redirect('/employe_dashboard')
        else:
            print("4444")
        return redirect('/')  

# register page
def register_page(request):
    return render(request,'register.html')

# register method
def register(request):
    print("***** 1 ")
    error = members.objects.member_validator(request.POST)
    if len(error) > 0:
        print("***** 2 ")
        for key, value in error.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/register_page')
    else:
        if request.method == "POST":
            print("***** 3 ")
            Register(request.POST, request.FILES)
            print("***** 4 ")
        return redirect('/')

# register customer page
def register_customer_page(request):
    return render(request,'register_customer.html')
# admin dashboard
def admin_dash(request):
    return render(request,'admin_dashboard.html')

# admin dashboard
def employe_dash(request):
    return render(request,'admin_dashboard.html')

# send ticket page
def send_ticket(request):
    return render(request,'send_ticket.html')