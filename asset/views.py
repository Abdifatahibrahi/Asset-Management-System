from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Furniture, Vehicle, FurnitureType, VehicleType
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
    
    # for i in appointment:
    #     a +=1

    mycontext = {
        'furnitures': f,
        'vehicles': v,
        # 'appointment': a,   
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


def delete_furniture(request, did):
    if not request.user.is_staff:
        return redirect('login')
    furniture = Furniture.objects.get(id=did)
    furniture.delete()
    return redirect('view_furnitures')


def add_furniture(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    furnituretypes = FurnitureType.objects.all()
    if request.method == 'POST':
        number = request.POST['serial_no']
        type = request.POST['type']
        date = request.POST['date']
        time = request.POST['time']
        i_value = request.POST['i_value']
        d_rate = request.POST['d_rate']
        d_rate = (int(d_rate) / 100)
        d_rate = float(d_rate)
        c_value = float(i_value) - (float(d_rate) * float(i_value))
        
        f1 = FurnitureType.objects.filter(type=type).first()

        try:
            Furniture.objects.create(serial_no=number, type=f1, date=date, time=time, 
                                     initial_value=i_value, depreciation_rate=float(d_rate),
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
        date = request.POST['date']
        i_value = request.POST['i_value']
        d_rate = request.POST['d_rate']
        d_rate = (int(d_rate) / 100)
        d_rate = float(d_rate)
        c_value = float(i_value) - (float(d_rate) * float(i_value))
        
        t = VehicleType.objects.filter(type=t_type).first()

        try:
            Vehicle.objects.create(number_plate=number, type=t, date=date, initial_value=i_value, depreciation_rate=float(d_rate),
                                     current_value=c_value)
            error = "no"
        
        except:
            error = "yes"
    d = {"error": error, 'types': vehicletypes}
    return render(request, 'add_vehicle.html', d)

