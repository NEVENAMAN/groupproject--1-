from django.shortcuts import render,redirect, HttpResponse
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
                return redirect('/admin_dashboard')
            else:
                return redirect('/employe_dashboard')
        else:
            print("4444")
        return redirect('/')  

def customer_login_page(request):
    return render(request,'customer_login_page.html')

def customer_page(request):
    if 'userid' in request.session:
        customer = customers.objects.get(id =request.session['userid'])
        employees = get_employees(request)
        context = {
            "customer" : customer,
            'employees': employees,
        }
        return render(request,'customer_page.html',context)
    else:
        return redirect('/customer_login_page')

# login method
def customer_login(request):
    error = customers.objects.customer_sigin_validator(request.POST)
    if len(error) > 0:
        print("***** 2 ")
        for key, value in error.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/customer_login')
    else:
        userId =  customer_Login(request)
        if userId != None:
            request.session['userid'] = userId
            return redirect('/customer_page') 
        else:
            return redirect('/customer_login_page')



# register page
def register_page(request):
    return render(request,'register.html')

# register method
def register(request):
    error = members.objects.member_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/register_page')
    else:
        if request.method == "POST":
            Register(request.POST, request.FILES)
        return redirect('/')

def register_client(request):
    error = customers.objects.customer_validation(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/register_customer')
    else:
        if request.method == "POST":
            Register_client(request.POST)
        return redirect('/')

# register customer page
def register_customer_page(request):
    return render(request,'register_customer.html')
# admin dashboard
def admin_dash(request):
    return render(request,'admin_dashboard.html')

# admin dashboard
def employe_dash(request):
    if 'userid' in request.session:
        employee = members.objects.get(id =request.session['userid'])
        context = {
            "employee" : employee,
        }
        return render(request,'employe_dashboard.html',context)
    else:
        return redirect('/login_page')


# send ticket page
def send_ticket(request,id):
    employee = members.objects.get(id=id)
    employees = get_employees(request)
    context = {
        "employee" : employee,
        "employees" : employees,
    }
    return render(request,'send_ticket.html', context)

def dashboard_page(request):
    id=request.session['userid']
    context={
        'employee':get_employee(request,id)
    }
    return render(request,'employe_dashboard.html',context)

def edit_login_page(request,id):
    if 'userid' in request.session:
        employee = members.objects.get(id=id)
        context = {
            "employee" : employee,
        }
        return render(request,'edit_login_page.html',context)
    else:
        return redirect('/login_page')

def edit_login_info(request,id):
    user_id = members.objects.get(id=id)
    error = members.objects.edit_login_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/edit_login_info/'+str(user_id.id))
    else:
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        edit_Login_data(id,email,password,confirm_password)
        return redirect('/dashboard_page')    

def employee_tickets(request,id):
    if 'userid' in request.session:
        employee = members.objects.get(id=id)
        employee_tickets = members.objects.get(id=id)
        tickets = employee_tickets.tickets.all()
        context = {
            "employee" : employee,
            "tickets" : tickets,
        }
        return render(request,'employee_tickets.html',context)
    else:
        return redirect('/login_page')

def del_ticket(request,id):
    delete_ticket(id)
    return redirect('/requests_page')

def del_employee_ticket(request,id):
    employee = members.objects.get(id = request.session['userid'])
    delete_ticket(id)
    return redirect('/employee_tickets/'+str(employee.id))

def view_ticket(request,id):
    employee = members.objects.get(id = request.session['userid'])
    ticket = get_ticket(id)
    print(ticket.full_name)
    context = {
        "employee" : employee,
        "ticket" :ticket,
    }
    return render(request,'view_ticket.html',context)

def send_employee_ticket(request):
    request.session['full_name'] = request.POST['full_name']
    employee_id= request.POST['employee_id']
    employee = members.objects.get(id=employee_id)
    error = members.objects.ticket_validation(request.POST)
    if len(error) > 0:
        print("***** 2 ")
        for key, value in error.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/send_ticket/'+str(employee.id))
    else:
        request.session['full_name'] = request.POST['full_name']
        full_name = request.POST['full_name']
        print(full_name)
        age = request.POST['age']
        identity_number = request.POST['identity_number']
        phone_number = request.POST['phone_number']
        telphone_number = request.POST['telphone_number']
        email = request.POST['email']
        state = request.POST['state']
        street = request.POST['street']
        service_desc = request.POST['service_desc']
        employee_Select = request.POST['employee']
        employee = members.objects.filter(first_name = employee_Select)
        add_ticket(full_name,age,identity_number,phone_number,telphone_number,email,state,street,service_desc,employee[0])
        return redirect('/welcome_page')

        
def welcome_page(request):
    customer = request.session['full_name']
    context = {
        "customer" : customer,
    }
    return render(request,'welcome_page.html',context)


def send_message_to_employee_page(request):
    if 'userid' in request.session:
        customer = customers.objects.get(id=request.session['userid'])
        employees = get_employee(request)
        context = {
            "employees":employees,
            'customer': customer,
        }
        return render(request,'send_message.html',context)
    else:
        return redirect('/login_page')

def messages_page(request, id):
    if 'userid' in request.session:
        employee = members.objects.get(id = id)
        messages_recieve =employee.messages_recieve.all()
        message_send = employee.message_send.all()
        context = {
            "employee" : employee,
            "messages_recieve" : messages_recieve,
            "message_send" : message_send, 
        }
        return render(request,'employee_messages.html',context)
    else:
        return redirect('/login_page')

def employee_send_message_method(request):
    error = Message.objects.message_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            Message.error(request, value, extra_tags=key)
        return redirect('/employee_send_message_page')
    else:
        sender = members.objects.filter( first_name = request.POST['send_from'])
        print(sender[0].first_name)
        message_context = request.POST['message_context']
        send_from = sender[0]
        reciver = customers.objects.filter(full_name = request.POST['send_to'])
        send_to = reciver[0]
        send_message(message_context,send_from,send_to)
    return redirect('/messages_page/'+ str(send_from.id))

def employee_send_message(request):
    if 'userid' in request.session:
        employee = members.objects.get(id=request.session['userid'])
        customers = get_all_customers(request)
        context = {
            "employee" : employee,
            "customers" : customers,
        }
        return render(request,'employee_send_message.html',context)
    else:
        return redirect('/login_page')

def view_message_data(request,id):
    if 'userid' in request.session:
        employee = members.objects.get(id=request.session['userid'])
        message = Message.objects.get(id=id)
        context = {
            "employee" :employee,
            "message" : message,
        }
        return render(request,'view_message_data.html',context)
    else:
        return redirect('/login_page')

def delete_message(request,id):
    message = Message.objects.get(id=id)
    del_message(message)
    return redirect('/messages_page/' + str(id))


def logout(request):
    request.session.flush()
    return redirect('/login_page')