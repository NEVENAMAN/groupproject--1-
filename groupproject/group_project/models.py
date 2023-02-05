from django.db import models
import  re
import bcrypt

class Usermanager(models.Manager):
    def member_validator(self, postData ):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        special_symbols = ['$','@','#','%','^','&']

        if len(postData['first_name']) < 3 :
            errors['first_name'] = "first name should be at least 3 characters"
        if len(postData['last_name']) < 3 :
            errors['last_name'] = "last name should be at least 3 characters"
        # if len(postData['user_level']) < 2:
        #     errors["user_level"] = "user_level should be at least 2characters"
        if len(postData['experience']) < 1:
            errors["experience"] = "experience should be at least 2characters"
        if len(postData['mobile_num']) < 9:
            errors["mobile_num"] = "number should be at least 9characters"
        if len(postData['address']) < 2:
            errors["Address"] = "Address should be at least 2characters"
        if len(postData['skill']) < 2:
            errors["skill"] = "skill should be at least 2characters"
        if len(postData['password']) < 8:
            errors["password"] = "user password should be at least 8characters"
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if not any(characters.isupper() for characters in postData['password']):
            errors['password_notInclude_upper'] = "Password must have at least one uppercase character"
        if not any(characters.islower() for characters in postData['password']):
            errors['password_notInclude_lower'] = "Password must have at least one lowercase character"
        if not any(characters.isdigit() for characters in postData['password']):
            errors['password_notInclude_number'] = "Password must have at least one numeric character."
        if not any(characters in special_symbols for characters in postData['password']):
            errors['password_symbol'] = "Password should have at least one of the symbols $@#%^&"
        if postData['password'] != postData['confirm_password']:
            errors['not_the_same'] = "please insert password similer as above"
        return errors

    def edit_login_validator(self, postData):
        error = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        special_symbols = ['$','@','#','%','^','&']
        if not email_regex.match(postData['email']) :
            error['email'] = "invaild email"
        if len(postData['password']) < 6:
            error['password_less_than'] = "Password must have atleast 6 characters"
        if len(postData['password']) > 20 :
            error['password_grather_than'] = "'Password cannot have more than 20 characters"
        if not any(characters.isupper() for characters in postData['password']):
            error['password_notInclude_upper'] = "Password must have at least one uppercase character"
        if not any(characters.islower() for characters in postData['password']):
            error['password_notInclude_lower'] = "Password must have at least one lowercase character"
        if not any(characters.isdigit() for characters in postData['password']):
            error['password_notInclude_number'] = "Password must have at least one numeric character."
        if not any(characters in special_symbols for characters in postData['password']):
            error['password_symbol'] = "Password should have at least one of the symbols $@#%^&"
        if postData['password'] != postData['confirm_password']:
            error['not_the_same'] = "please insert password similer as above"
        return error
    
    def sigin_validator(self, postData):
        error = {}
        userid = members.objects.filter(email = postData['email'])
        print(postData['email'])
        if len(userid) == 0 :
            error['user_not_found'] = "user not exisit"
            return error
        user = userid[0]
        if (bcrypt.checkpw(postData['password'].encode(), user.password.encode()) != True):
            error['incorrect_password'] = "you insert password error"
        return error
    
    def customer_validation(self, postData):
        errors= {}
        special_symbols = ['$','@','#','%','^','&']
        if len(postData['full_name']) < 5:
            errors["full_name"] = "name should be at least 5 characters"
        if len(postData['address']) < 5:
            errors["address"] = "Address should be at least 5 characters"
        if len(postData['mobile_num']) < 9:
            errors["mobile_num"] = "number should be at least 9 characters"
        if len(postData['identity_num']) < 9:
            errors["identity_num"] = "scope of work should be at least 9 characters"
        if len(postData['password']) < 8:
            errors["password"] = "user password should be at least 8characters"
        if not any(characters.isupper() for characters in postData['password']):
            errors['password_notInclude_upper'] = "Password must have at least one uppercase character"
        if not any(characters.islower() for characters in postData['password']):
            errors['password_notInclude_lower'] = "Password must have at least one lowercase character"
        if not any(characters.isdigit() for characters in postData['password']):
            errors['password_notInclude_number'] = "Password must have at least one numeric character."
        if not any(characters in special_symbols for characters in postData['password']):
            errors['password_symbol'] = "Password should have at least one of the symbols $@#%^&"
        if postData['password'] != postData['confirm_password']:
            errors['not_the_same'] = "please insert password similer as above"
        return errors

    def ticket_validation(self, postData):
        errors = {}
        if len(postData['full_name']) < 5:
            errors["full_name"] = "name should be at least 5 characters"
        if len(postData['phone_number']) < 9:
            errors["phone_number"] = "number should be at least 9 characters"
        if len(postData['identity_number']) < 9:
            errors["identity_number"] = "scope of work should be at least 9 characters"
        if len(postData['service_desc']) < 5:
            errors["service_desc"] = "name should be at least 5 characters"
        if len(postData['employee']) < 5:
            errors["employee"] = "name should be at least 5 characters"
        return errors 

    def message_validator(self, postData):
        error = {}
        if len(postData['send_from']) < 3 :
            error['send_from'] = "sender should be at least 3 characters "
        if len(postData['message_context']) < 1 :
            error['message_context'] = "message should be at least 1 characters "
        if len(postData['send_to']) < 3 :
            error['send_to'] = " should select reciever "
        return error
        
class userLevel(models.Model):
    name = models.CharField(max_length=255,unique=True)
    # members = list of members
    created_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 

class members(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    skill=models.CharField(max_length=255)
    experience=models.IntegerField()
    address=models.CharField(max_length=255)
    mobile_num=models.IntegerField()
    password=models.CharField(max_length=255)
    user_level=models.ManyToManyField(userLevel , related_name="members")
    identity_image = models.FileField(upload_to="identity_images/", max_length=250,null=True,blank=True,default='')
    created_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # tickets = list of tickets
    objects = Usermanager()

class tickets(models.Model):
    full_name = models.CharField(max_length=255)
    identity_number = models.IntegerField()
    age = models.IntegerField()
    phone_number = models.CharField(max_length=255)
    telphone_number = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    service_desc = models.TextField()
    employee = models.ForeignKey(members , related_name="tickets" , on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class customers(models.Model):
    full_name = models.CharField(max_length=255)
    identity_number = models.IntegerField(unique=True)
    mobile_num = models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    message_context = models.TextField()
    send_to = models.ForeignKey(members, related_name="messages_recieve" , on_delete=models.DO_NOTHING)
    send_from = models.ForeignKey(members , related_name="message_send" , on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = Usermanager()



# member table method --------------------------------------------------------------------------------
# register new member
def Register(data, files):
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    skill = data['skill']
    experience = data['experience']
    address = data['address']
    mobile_num = data['mobile_num']
    password =data['password']
    identity_image = files['identity_image']
    # user_level_id = data.get('user_level',False)
    # if user_level_id==False:
    #     user_level = userLevel.objects.get(name='employee')
    # else:
    #     user_level =  userLevel.objects.get(id=user_level_id)
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    if (data['confirm_password'] == password):
        members.objects.create(first_name = first_name , last_name = last_name, email = email , skill=skill , experience=experience , address=address ,mobile_num=mobile_num , identity_image = identity_image , password = pw_hash)

# login current user
def Login(request):
    user = members.objects.filter(email = request.POST['email'])
    if user:
        loged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), loged_user.password.encode()):
            request.session['userid'] = loged_user.id
            return loged_user.id
    else:
        return None

# get all employee
def get_employees(request):
    return members.objects.all()

# tickets table method --------------------------------------------------------------------------------
def add_ticket(full_name,age,identity_number,phone_number,telphone_number,email,state,street,service_desc, employee):
    return tickets.objects.create(full_name = full_name,age=age,identity_number=identity_number,phone_number=phone_number,telphone_number=telphone_number,email=email,state=state,street=street,service_desc=service_desc,employee=employee)


def get_employee(request,id):
    return members.objects.get(id=id)



def edit_Login_data(id,email,password,confirm_password):
    user = members.objects.get(id=id)
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    if(password == confirm_password):
        user.password = pw_hash
        user.email = email
    return user.save()

def get_all_tickets(request):
    return tickets.objects.all()

def get_ticket(id):
    return tickets.objects.get(id=id)

def delete_ticket(id):
    ticket = tickets.objects.get(id=id)
    return ticket.delete()

def send_message(message_context,send_from,send_to):
    return Message.objects.create(message_context = message_context , send_from = send_from , send_to = send_to)

def del_message(message):
    return message.delete()