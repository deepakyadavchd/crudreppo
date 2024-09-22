from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, update_session_auth_hash, login
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext as _
from django.contrib import messages
from .models import*
# Create your views here.

def createview(request):

    if(request.POST.get("createbtn")):
        srollno = request.POST["rtxt"]
        sname = request.POST["ntxt"]
        smarks = request.POST["mtxt"]
        sresult = request.POST["rltxt"]

        if(  srollno =="" and sname =="" and smarks =="" ):
            er= {"error":" Enter All Details "}
            return  render(request, 'create.html', context=er)
      
        elif(srollno==""and sname=="" ):
            er= {"errorx":" Enter Roll no and name "}
            return render(request, 'create.html', context=er)
        
        elif(sname==""and smarks=="" ):
            er= {"errorxz":" Enter name and marks"}
            return render(request, 'create.html', context=er)
        
        elif(srollno==""and smarks=="" ):
            er= {"errorv":" Enter Roll no and marks "}
            return render(request, 'create.html', context=er)
        
        elif(sname=="" ):
            er= {"errorx":" Enter  Name "}
            return render(request, 'create.html', context=er)
        
        elif(srollno=="" ):
            er= {"errorx":" Enter Roll no "}
            return render(request, 'create.html', context=er)
        
        elif(smarks=="" ):
            er= {"errorv":" Enter marks "}
            return render(request, 'create.html', context=er)
        
        
        sobj = Students_bca(studentrolln=srollno, studentname=sname, studentmarks=smarks, studentresult=sresult)
        sobj.save()

    if(request.POST.get("createbtn")):
            mess={"msg": "Thankyou , Your Details Recorded"}
            return render(request, 'create.html', context=mess)
    return render(request, 'create.html')
            
def resultview(request):
    if(request.POST.get("srchbtn")):
        rl = request.POST.get("inputtxt")
        mems = Students_bca.objects.filter(studentrolln=rl)
        
        l = len(mems)
        if l==0:
            data={"min":" Record not found "}

        if l=="" :   
            data={"queryset":"enter rollno "}
        else:
            data={"queryset":mems}
        return render(request, 'results.html', context=data)
    
    mems=Students_bca.objects.all()
    l = len(mems)
    if l==0:
        data={"min":" Record not found "}
    else:
        data={"queryset":mems}
    return render(request, 'results.html', context=data)

def detailsview(request):
    roll = request.GET.get("rt")
    mems=Students_bca.objects.filter(studentrolln=roll)
    data={"queryset":mems}
    return render(request, 'detail.html', context=data)

def deleteview(request):
    roll = request.GET.get("rt")
    Students_bca.objects.filter(studentrolln=roll).delete()
    return redirect("../result")

def editview(request):
    
    
    roll = request.GET.get("rt")
    queryset=Students_bca.objects.filter(studentrolln=roll).first()
    data={"qs":queryset}
    
    
    if(request.POST.get("upbtn")):
        rollno = request.POST["txtrollno"]
        name = request.POST["txtname"]
        marks = request.POST["txtmarks"]
        Students_bca.objects.filter(studentrolln=roll).update(studentrolln=rollno,studentname=name,studentmarks=marks)
       
        
        return redirect("../result")
    return render(request, 'update.html', context=data )


def signin(request):
    if(request.POST.get("btnlogin")):
       userid = request.POST["txtuserid"]
       passwprd = request.POST["txtpassword"]
       user = authenticate(username=userid,  password=passwprd)

       if user:
           login(request, user)   # to store userid in session
           username = user.username
           data = {
               "username" : user.username
           }
           return render(request, 'welcome.html', context=data)
       else:
           data = {
               "error" : "Invalid email and pasword"
           }

           return render(request, 'signin.html', context=data)


    return render(request, 'signin.html')



def signup(request):
    if(request.POST.get("createbtn")):
        f_name = request.POST["txtfname"]
        l_name = request.POST["txtlname"]
        email_id= request.POST["txtemail"]
        passwd = request.POST["txtpassword"]

        user = User(first_name=f_name, last_name=l_name, email=email_id,
        username=email_id, is_staff=True, is_superuser=True)
        user.set_password(passwd)
        user.save()

        if(request.POST.get("createbtn")):
            mess={"msg": "Congratulations, your account has been successfully created ."}
            return render(request, 'create.html', context=mess)
        
    return render(request, 'signup.html')

def logoutview(request):
    logout(request)
    return redirect("../signin")

    

def passchange(request):
    if request.method =="POST":
        form =PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            congrats = {
               "message" :"password changed successfully"}
            return render(request, 'welcome2.html', context=congrats)
        
    else:
        form =PasswordChangeForm (user=request.user)
    return render(request, 'passup.html', {'form': form})
        
