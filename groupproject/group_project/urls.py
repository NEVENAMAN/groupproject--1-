from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('admin_dashboard',views.admin_dash),
    path('employe_dashboard',views.employe_dash),
    path('login_page',views.login_page),
    path('login',views.login),
    path('logout',views.logout),
    path('customer_login_page', views.customer_login_page),
    path('customer_login', views.customer_login),
    path('customer_page', views.customer_page),
    path('register_page',views.register_page),
    path('register',views.register),
    path('register_client', views.register_client),
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
    path('send_message_page',views.send_message_to_employee_page),
    path('employee_send_message',views.employee_send_message),
    path('messages_page/<int:id>',views.messages_page),
    path('employee_send_message_method',views.employee_send_message_method),
    path('view_message_data/<int:id>',views.view_message_data),
    path('delete_message/<int:id>',views.delete_message),
    path('welcome_page',views.welcome_page),
    path('members_page',views.member_page),
    path('delete_member/<int:id>',views.del_member),
    path('view_members/<int:id>',views.view_member),
    path('customer_messages_page/<int:id>',views.customer_messages_page),
    path('customer_view_message_data/<int:id>',views.customer_view_message_data)



]