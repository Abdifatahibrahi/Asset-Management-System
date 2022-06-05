from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Furniture, Vehicle, FurnitureType, VehicleType, ElectronicType, Electronic
from .forms import FurnitureForm

# Create your views here.



def Home(request):
    doctors = Furniture.objects.all()
    return render(request, 'home.html',{
        "doctors": doctors
    }) 


def About(request):
    return render(request, 'about.html') 


def Contact(request):
    return render(request, 'contact.html') 

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    
    furniture = Furniture.objects.all()
    vehicle = Vehicle.objects.all()
    electronics = Electronic.objects.all()
    # appointment = Appointment.objects.all()
    d=0
    p=0
    a=0

    # for f in furniture:
    #     f +=1
    f = len(furniture)

    # for i in patient:
    #     p +=1
    v = len(vehicle)
    
    e = len(electronics)
    
    assets = [f, v, e]

    mycontext = {
        'furnitures': f,
        'vehicles': v,
        'electronics': e,   
    }
    return render(request, 'index.html', mycontext)

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, 'login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('admin_login')


def view_furniture(request):
    if not request.user.is_staff:
        return redirect('login')
    fur = Furniture.objects.all()
    
    f = {'fur': fur}
    return render(request, 'view_furniture.html', f)


def delete_furniture(request, s_no):
    if not request.user.is_staff:
        return redirect('login')
    furniture = Furniture.objects.get(serial_no=s_no)
    furniture.delete()
    return redirect('view_furnitures')

# def ChairPref(number):
#     string_x = 'CH'+ str(number)
#     return string_x

# def CupboardPref(number):
#     string_x = 'CB'+ str(number)
#     return string_x
    
# def TablePref(number):
#     string_x = 'TB'+ str(number)
#     return string_x
    
    
def add_furniture(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    furnituretypes = FurnitureType.objects.all()
    if request.method == 'POST':
        type = request.POST['type']
        i_value = request.POST['i_value']
        rate = 0.11
        c_value = float(i_value) - (rate * float(i_value))
        
        f1 = FurnitureType.objects.filter(type=type).first()
        
        try:
            # serial_no=number,
            Furniture.objects.create(type=f1,
                                        initial_value=i_value, depreciation_rate=rate,
                                     current_value=c_value)
            error = "no"
        
        except:
            error = "yes"
    d = {"error": error, 'types': furnituretypes}
    return render(request, 'add_furniture.html', d)


# def add_furniture(request):
#     error = ""
#     if not request.user.is_staff:
#         return redirect('login')
#     furnituretypes = FurnitureType.objects.all()
    
#     form = FurnitureForm(request.POST)
    
#     if form.is_valid():
#         error = "no"
#         form.save()
#     else:
#         error = "yes"
#         print(error)
#     d = {"error": error,'types': furnituretypes}
#     return render(request, 'add_furniture.html', d)
    
        
    


# Vehicles

def view_vehicles(request):
    if not request.user.is_staff:
        return redirect('login')
    veh = Vehicle.objects.all()
    f = {'veh': veh}
    return render(request, 'view_vehicles.html', f)


def delete_vehicle(request, did):
    if not request.user.is_staff:
        return redirect('login')
    vehicle = Vehicle.objects.get(id=did)
    vehicle.delete()
    return redirect('view_vehicles')


def add_vehicle(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    vehicletypes = VehicleType.objects.all()
    if request.method == 'POST':
        number = request.POST['plate']
        t_type = request.POST['type']
        i_value = request.POST['i_value']
        rate = 0.01
        c_value = int(float(i_value) - (rate * float(i_value)))
        
        t = VehicleType.objects.filter(type=t_type).first()

        try:
            Vehicle.objects.create(number_plate=number, type=t, initial_value=i_value, depreciation_rate=rate,
                                     current_value=c_value)
            error = "no"
        
        except:
            error = "yes"
    d = {"error": error, 'types': vehicletypes}
    return render(request, 'add_vehicle.html', d)



# Electronics

def view_electronics(request):
    if not request.user.is_staff:
        return redirect('login')
    elec = Electronic.objects.all()
    f = {'elec': elec}
    return render(request, 'view_electronics.html', f)


def delete_Electronics(request, did):
    if not request.user.is_staff:
        return redirect('login')
    elec = Electronic.objects.get(id=did)
    elec.delete()
    return redirect('view_vehicles')


def add_Electronics(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    electronictype = ElectronicType.objects.all()
    if request.method == 'POST':
        number = request.POST['serial_no']
        t_type = request.POST['type']
        i_value = request.POST['i_value']
        rate = 0.1
        c_value = int(float(i_value) - (rate * float(i_value)))
        
        t = ElectronicType.objects.filter(type=t_type).first()

        try:
            Electronic.objects.create(serial_no=number, type=t, initial_value=i_value, depreciation_rate=rate,
                                     current_value=c_value)
            error = "no"
        
        except:
            error = "yes"
    d = {"error": error, 'types': electronictype}
    return render(request, 'add_electronic.html', d)

