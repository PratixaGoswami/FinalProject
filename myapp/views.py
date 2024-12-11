from django.shortcuts import render,redirect
from .forms import*
from django.contrib.auth import logout
from django.core.mail import send_mail
import random
from livepro  import settings



# Create your views here.
def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})
def login(request):
    msg=''
    if request.method=="POST":
        unm=request.POST['username'] 
        pas=request.POST['password']
        
        user=usersignup.objects.filter(username=unm,password=pas)

        uid=usersignup.objects.get(username=unm)
        print("Userid:",uid.id)

        if user:
            print("Login successfully!")
            msg='Login successfully!'
            request.session['user']=unm
            request.session['uid']=uid.id

            return redirect("/")
        else:
            print("Error!Login faild...")
            msg="Error! Login faild..."    


    return render(request,'login.html',{'msg':msg})
def signup(request):
    msg=""
    if request.method=='POST':
        global vldreq
        vldreq=usersignupform(request.POST)
        username=""
        if vldreq.is_valid():
            username=vldreq.cleaned_data.get('username')
            try:
                usersignup.objects.get(username=username)
                print("username is already exists!")
                msg="Username is already exists!"
            except usersignup.DoesNotExist:
                
                print("Signup successfully!")
            

                global otp
                otp=random.randint(11111,99999)
                sub="your one time password"
                msg=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nNotesApp Tech - Rajkot\n+91 9737439749 | pratixagosai2000@gmail.com"
                from_id=settings.EMAIL_HOST_USER
                to_id=[request.POST['username']]
                send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
                #send_mail(subject="one time password",message=f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nNotesApp Tech - Rajkot\n+91 9737439749 | pratixagosai2000@gmail.com",from_email=settings.EMAIL_HOST_USER,recipient_list=['pratixagoswami2000@gmail.com'])
            
                return redirect('otpverify')
            
        else:
            print(vldreq.errors)    
    return render(request,'signup.html',{'msg':msg})
def userlogout(request):
    logout(request)
    return redirect('login')
    
def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user}) 
def contact(request):
    user=request.session.get('user')
    if request.method=='POST':
        cdata=contactform(request.POST)
        if cdata.is_valid():
            cdata.save()

            #email sending
            sub="Thankyou!"
            msg=f"Hello User!\n\nThanks for connecting with us!\nWe will contact you shortly!\n\nThanks & Regards\n+919737439749| pratixagosai2000@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
 
            print("contact data has been saved")
            
        else:
            (cdata.errors)    
    return render(request,'contact.html',{'user':user})  
def notes(request):
    msg=""
    user=request.session.get('user')
    if request.method=='POST':
        notedata=noteform(request.POST,request.FILES)
        if notedata.is_valid():
            notedata.save()
            print("Your notes has been submitted")
            msg="Your notes has been submitted"
        else:
            print(notedata.errors)
            msg="Error!Somthing went wrong...Try again!"
    return render(request,'notes.html',{'user':user,'msg':msg}) 
def profile(request):
    msg=""
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=usersignup.objects.get(id=uid)
    if request.method=='POST':
        upreq=usersignupform(request.POST,instance=cuser)
        if upreq.is_valid():
            upreq.save()
            print("Update your Profile successfully")
            msg="Update your Profile successfully"
            return redirect('/')
        else :
            print(upreq.errors)   
            msg="Error! Something is wrong"

    return render(request,'profile.html',{'user':user,'cuser':cuser,'msg':msg})

def otpverify(request):
    msg=""
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            print("verification done!")
            vldreq.save() 
            
            return redirect('login')
        else:
            print("Error!Invalid OTP")
            msg="Error!Invalid OTP"

    return render(request,'otpverify.html',{'msg':msg})
