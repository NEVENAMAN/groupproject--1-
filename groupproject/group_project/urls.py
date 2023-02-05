from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('admin_dashboard',views.admin_dash),
    path('employe_dashboard',views.employe_dash),
    path('login_page',views.login_page),
    path('login',views.login),
    path('register_page',views.register_page),
    path('register',views.register),
    path('register_customer',views.register_customer_page),
    path('send_ticket/<int:id>',views.send_ticket),
    path('dashboard_page',views.dashboard_page),
    path('edit_login_info/<int:id>',views.edit_login_info),
    path('edit_login_page/<int:id>',views.edit_login_page),
    path('view_ticket/<int:id>',views.view_ticket),
    path('del_employee_ticket/<int:id>',views.del_employee_ticket),
    path('delete_ticket/<int:id>',views.del_ticket),
    path('employee_tickets/<int:id>',views.employee_tickets),
    path('send_employee_ticket',views.send_employee_ticket),
    path('send_message_page',views.send_message_page),
    path('messages_page/<int:id>',views.messages_page),
    path('send_message_method',views.send_message_method),
    path('view_message_data/<int:id>',views.view_message_data),
    path('delete_message/<int:id>',views.delete_message),
    path('welcome_page',views.welcome_page),
]