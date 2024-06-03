from django.shortcuts import render,redirect
from .models import farmer,scholar
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def farmerlogin(request):
  return render(request,"farmer/farmerlogin.html",{})

def scholarlogin(request):
  return render(request,"scholar/scholarlogin.html",{})

def add_farmer(request):
  if request.method == "POST":
    farmer_name = request.POST.get("Farmer_name")
    contact_num = request.POST.get("Contact_num")
    email_id = request.POST.get("Email_id")
    password = request.POST.get("Password")
    f = farmer()
    f.Farmer_name = farmer_name
    f.Contact_num = contact_num
    f.Email_id = email_id
    f.Password = password
  # f.save()
  # checking existing -
    check_existing = farmer.objects.filter(Farmer_name=farmer_name) and farmer.objects.filter(Contact_num = contact_num) and farmer.objects.filter(Email_id = email_id) and farmer.objects.filter(Password = password).exists()
    if check_existing:
      messages.error(request,"The email address is already in use by another account.!! Please login...")
      return redirect('/login/farmerlogin/')
  
    else:
      f.save()
      messages.success(request,'Your Account has been created successfully!!')
    # return redirect('login/farmerlogin/')
      return redirect('/farmerUI/')



def loginfarmer(request):
    if request.method == "POST":
        emailid = request.POST.get("EmailId")
        password1 = request.POST.get("Logpassword")

        # Check if both email and password match an existing farmer
        try:
            farmer_obj = farmer.objects.get(Email_id=emailid, Password=password1)
        except farmer.DoesNotExist:
            messages.error(request, "Please enter a valid email or password.")
            return redirect('/login/farmerlogin/')
        else:
            request.session['id'] = farmer_obj.id
            request.session['Farmer_name'] = farmer_obj.Farmer_name
            request.session['Email_id'] = farmer_obj.Email_id
            messages.success(request, 'Logged In Successfully!!')
          
            return redirect('/farmerUI/')
    else:
        return redirect('/login/farmerlogin/')
  

# scholar form validation :-
def add_scholar(request):
  if request.method == "POST":
    scholar_name = request.POST.get("Scholar_name")
    contact_num = request.POST.get("Contact_num")
    email_id = request.POST.get("Email_id")
    password = request.POST.get("Password")
  s = scholar()
  s.Scholar_name = scholar_name
  s.Contact_num = contact_num
  s.Email_id = email_id
  s.Password = password
  # checking existing -
  check_existing = scholar.objects.filter(Scholar_name=scholar_name) and scholar.objects.filter(Contact_num = contact_num) and scholar.objects.filter(Email_id = email_id) and scholar.objects.filter(Password = password).exists()
  if check_existing:
    messages.error(request,"The email address is already in use by another account.!! Please login...")
    return redirect('/scholar/')

  else:
    s.save()
    messages.success(request,'Your Account has been created successfully!! Please login')
    return redirect('/login/scholarlogin/')
  
def loginscholar(request):
    if request.method == "POST":
        emailsc = request.POST.get("scholarEmail")
        passw = request.POST.get("scholarPassword")

        # Check if both email and password match an existing scholar
        try:
            scholar_obj = scholar.objects.get(Email_id=emailsc, Password=passw)
        except scholar.DoesNotExist:
            messages.error(request, "Please enter a valid email or password.")
            return redirect('/login/scholarlogin/')
        else:
            request.session['Scholar_name'] = scholar_obj.Scholar_name
            request.session['Email_id'] = scholar_obj.Email_id
            messages.success(request, 'Logged In Successfully!!')
            return redirect('/scholar/')
    else:
        return redirect('/login/scholarlogin/')