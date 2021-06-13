from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import HomePage,Admin_reg, Notice_view, Profile_view, Complaint_view
# Create your views here.
import smtplib
import email.message
from smtplib import SMTP 

import random
def Index(request):
    return HttpResponse('<h1>Hello python class</h1>')

def Dashboard(request):
    return render(request,'login_details/Dashboard.html') 

def Admindashboard(request):
    return render(request,'login_details/Admindashboard.html') 

def Home(request):
    return render(request,'login_details/Home.html') 

def Admindash(request):
    return render(request,'login_details/Admindash.html') 

def Viewcomplaint(request):
    return render(request,'login_details/Viewcomplaint.html') 

def  Viewnotice(request):
    return render(request,'login_details/Viewnotice.html') 
    
def  Viewprofile(request):
    return render(request,'login_details/Viewprofile.html') 

def  Notice(request):
   try:
    if 'User' in request.session.keys():
        data = request.session['User']
        user = Admin_reg.objects.get(aname = data)
        if request.POST:
            obj = Notice_view()
            obj.NName= user
            obj.Nemail = request.POST['email']   
            obj.Nnotice = request.POST['Notice']
            obj.Nsubject = request.POST['noticesubject']
            obj.Nphone = request.POST['phone']
            obj.Ndate = request.POST['date']
            obj.save()
            return redirect('disnotice_data')
            return render(request,'login_details/Notice.html',{'key_user':user})
        else:
            return redirect('sign')
   except:

    return render(request,'login_details/Notice.html') 

def Disnotice_data(request):
    if 'User' in request.session.keys():
        data = request.session['User']
        user = Admin_reg.objects.get(aname = data)
        notice = Notice_view.objects.filter(NName = user)
        return render(request,'login_details/Viewnotice.html',{'notice':notice,'new_user':user})
    else:
        return redirect('Admindashboard')

def  Profile(request):
#    try:
#     if 'User' in request.session.keys():
#             data = request.session['User']
#             user = Admin_reg.objects.get(aname = data)
#             if request.POST:
#                 obj = Profile_view()
#                 obj.PName = user
#                 obj.Pemail = request.POST['email']   
#                 obj.Pflattype = request.POST['Flat_Type']
#                 obj.Pflatno = request.POST['FlatNo']
#                 obj.Pphoto = request.FILES['photo']
#                 obj.save()
#                 return redirect('disprofile_data')
#             return render(request,'login_details/Profile.html',{'key_user':user})
#     else:
#         return redirect('sign')
#    except:
#     return render(request,'login_details/Profile.html')
 try:
    if 'User' in request.session.keys():
            data = request.session['User']
            user = Admin_reg.objects.get(aname = data)
            if request.POST:
                obj = Profile_view()
                obj.PName = user
                obj.Pemail = request.POST['email']   
                obj.Pflattype = request.POST['Flat_Type']
                obj.Pflatno = request.POST['FlatNo']
                obj.Pphoto = request.FILES.get('photo')  
                obj.save()
                return redirect('disprofile_data')
            return render(request,'login_details/Profile.html',{'key_user':user})
    else:
            return redirect('sign')
 except:
    if 'User' in request.session.keys():
            data = request.session['User']
            user = HomePage.objects.get(uName = data)
            if request.POST:
                obj = Profile_view()
                obj.PNAme = user
                obj.Pemail = request.POST['email']   
                obj.Pflattype = request.POST['Flat_Type']
                obj.Pflatno = request.POST['FlatNo']
                obj.Pphoto = request.FILES.get('photo')  
                obj.save()
                return redirect('disprofile_data')
            return render(request,'login_details/Profile.html',{'key_user':user})
    else:
            return redirect('sign')


def Disprofile_data(request):
 try:
   if 'User' in request.session.keys():
        data = request.session['User']
        user = Admin_reg.objects.get(aname = data)
        Profile1 = Profile_view.objects.filter(PName = user)
        return render(request,'login_details/Viewprofile.html',{'Profile1':Profile1,'new_user':user})
   else:
        return redirect('Admindashboard')
 except:
    if 'User' in request.session.keys():
            data = request.session['User']
            user = HomePage.objects.get(uName = data)

            Profile1 = Profile_view.objects.filter(PName = user)
            return render(request,'login_details/Viewprofile.html',{'Profile1':Profile1,'new_user':user})
    else:
            return redirect('Admindashboard')
def complaint(request):
   try: 
    if 'User' in request.session.keys():
        data = request.session['User']
        user = Admin_reg.objects.get(aname = data)
        if request.POST:
            obj = Complaint_view()
            obj.CName= user
            obj.Cemail = request.POST['email']   
            obj.Cmessage = request.POST['message']
            obj.Ccategorytpe = request.POST.get('categorytype')
            obj.Ccategory = request.POST['category']
            obj.Cphone = request.POST['phone']
            # obj.Cdate = request.POST['date']
            obj.save()
            return redirect('discomplaint_data')
        return render(request,'login_details/complaint.html',{'key_user':user})
    else:
        return redirect('sign')
   except:
    return render(request,'login_details/complaint.html') 

def Discomplaint_data(request):
    if 'User' in request.session.keys():
        data = request.session['User']
        user = Admin_reg.objects.get(aname = data)
        complaint = Complaint_view.objects.filter(CName = user)
        return render(request,'login_details/Viewcomplaint.html',{'complaint':complaint,'new_user':user})
    else:
        return redirect('Admindashboard')

def  loginlog(request):
    userlog= HomePage.objects.all()  
    return render(request,'login_details/loginlog.html',{'userlog':userlog}) 

def SignIn(request):
    if request.POST:
        name  = request.POST.get('usname')
        Email = request.POST['email']
        psw = request.POST['password2']
        phone = request.POST.get('phonen')
        cpassword   = request.POST.get('confpassword')
        
        print(name ,Email,cpassword, psw, phone)

        obj = HomePage()
        obj.uName = name
        obj.Email =  Email
        obj.password = psw
        obj.cpassword  = cpassword 
        obj.phonen = phone
        obj.save()

    return render(request,'login_details/SignIn.html')
    
def admin(request):
    if request.POST:
        uname  = request.POST.get('username')
        Email = request.POST['email']
        psw = request.POST['password2']
        cpassword   = request.POST.get('confpassword')
        aphone =request.POST.get('phonen')
        
        print(uname ,Email,cpassword, psw, aphone)

        obj = Admin_reg()
        obj.aname = uname
        obj.aEmail =  Email
        obj.apassword = psw
        obj.acpassword  = cpassword 
        obj.aphone = aphone
        obj.save()

    return render(request,'login_details/SignIn.html')

def Singup(request):
    if request.method == "POST":
        try:
            print(request.POST.get('usname'))
            print(request.POST['password2'])
            m = HomePage.objects.get(uName = request.POST.get('usname'))
            if m.password == request.POST['password2']:
                print(m.Email)
                request.session['User'] = m.uName
                return redirect('home')
            else:
                return HttpResponse("<h2><a href=''>You have entered wrong password</a></h2>")
        except:
            h= Admin_reg.objects.get(aname = request.POST.get('usname'))
            if h.apassword == request.POST['password2']:
                        print(h.aEmail)
                        request.session['User'] = h.aname
                        return redirect('home')
            return HttpResponse("<h2><a href=''>no username found.</a></h2>")
    return render(request,'login_details/SignIn.html')

def Forget(request):
    if request.POST:
        email1 = request.POST.get('email23')
        number1 = request.POST.get('numbar23')
            
        try:
            valid = HomePage.objects.get(Email=email1)
            if int(valid.phone) == int(number1):
                print(email1)
                request.session['useremail'] = email1
                numbers = [1,2,5,6,7,8,9]
                num = ""
                for i in range(4):
                    num += str(random.choice(numbers))
                
                num = int(num)
                print(num)
                # ============== Email ==============
                sender_email = "techmahek7@gmail.com"  
                sender_pass = "future17@"
                receiver_email = email1 
                server = smtplib.SMTP('smtp.gmail.com',587)
                your_message =  "This Is Your OTP Number = "+str(num)
                print(your_message)
                msg = email.message.Message()
                msg['Subject'] = "Your OTP From Online Society Management System"
                msg['From'] = sender_email
                msg['To'] = receiver_email
                password = sender_pass
                msg.add_header('Content-Type','text/html')
                msg.set_payload(your_message)

                server.starttls()
                server.login(msg['From'],password)
                server.sendmail(msg['From'],msg['To'],msg.as_string())
                # ============== End Email ===========
                request.session['otp'] = num
                return redirect('Otp')
                                    
            else:
                return HttpResponse("<h2><a href=''>Mobile Number Is Not Registered</a></h2>")
        except:
            valid = Admin_reg.objects.get(aEmail=email1)
            if int(valid.aphone) == int(number1):
                print(email1)
                request.session['useremail'] = email1
                numbers = [1,2,5,6,7,8,9]
                num = ""
                for i in range(4):
                    num += str(random.choice(numbers))
                
                num = int(num)
                print(num)
                # ============== Email ==============
                sender_email = "techmahek7@gmail.com"  
                sender_pass = "future17@"
                receiver_email = email1 
                server = smtplib.SMTP('smtp.gmail.com',587)
                your_message =  "This Is Your OTP Number = "+str(num)
                print(your_message)
                msg = email.message.Message()
                msg['Subject'] = "Your OTP From Online Society Management System"
                msg['From'] = sender_email
                msg['To'] = receiver_email
                password = sender_pass
                msg.add_header('Content-Type','text/html')
                msg.set_payload(your_message)

                server.starttls()
                server.login(msg['From'],password)
                server.sendmail(msg['From'],msg['To'],msg.as_string())
                # ============== End Email ===========
                request.session['otp'] = num
                return redirect('Otp')
                                    
            else:
                return HttpResponse("<h2><a href=''>Mobile Number Is Not Registered</a></h2>")
        
    return render(request,'login_details/Forget.html')

def Otp(request):
    if 'otp' in request.session.keys():
        if request.POST:
            otP = request.POST.get('otp')
            if str(otP) == str(request.session['otp']):
                del request.session['otp']
                return redirect('newpassword')
            else:
                return render(request,'login_details/Forget.html')  
        return render(request,'Otp.html')
    else:
        return render(request,'login_details/Forget.html')    

def newpassword(request):
   try:
    if request.session.has_key('useremail'):
        if request.POST:
            pass_1 = request.POST['password1']
            pass_2 = request.POST['password2']
            
            if pass_1 == pass_2:
                valid = HomePage.objects.get(Email=request.session['useremail'])
                valid.password = pass_2
                valid.save()
                del request.session['useremail']
                return redirect('sign')
            else:
                return HttpResponse("<h2><a href=''>Passwords Are Not Same ...</a></h2>")
        return render(request,'login_details/newpassword.html')
   except: 
    if request.session.has_key('useremail'):
        if request.POST:
            pass_1 = request.POST['password1']
            pass_2 = request.POST['password2']
            
            if pass_1 == pass_2:
                valid = Admin_reg.objects.get(aEmail=request.session['useremail'])
                valid.apassword = pass_2
                valid.save()
                del request.session['useremail']
                return redirect('sign')
            else:
                return HttpResponse("<h2><a href=''>Passwords Are Not Same ...</a></h2>")
        return render(request,'login_details/newpassword.html')
    
    return render(request,'login_details/newpassword.html')
