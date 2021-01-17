from django.shortcuts import render,HttpResponse
import requests
from vaccine_app.models import Booking
# Create your views here.

def index(request):
    # API to get the data 
    URL = "https://corona.lmao.ninja/v2/countries/India"

    # sending get request and saving the response as response object 
    r = requests.get(url = URL)  

    liveData = r.json()

    data = {}
    data["population"] = f'{liveData["population"]:,}'
    data["totalCases"] = f'{liveData["cases"]:,}'
    data["totalRecovered"] = f'{liveData["recovered"]:,}'
    data["totalDeaths"] = f'{liveData["deaths"]:,}'
    print(data)
    return render(request,'index.html',data)

def hospital_data(request):
    return render(request, 'hospital_data.html')


def booking(request):
    if(request.method == 'POST'):
        try:
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            address = request.POST.get('address')
            vaccination_center = request.POST.get('center')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip')

            datadict = {
                "first_name":first_name,
                "last_name":last_name,
                "email":email,
                "phone":phone,
                "age":age,
                "gender":gender,
                "address":address,
                "vaccination_center":vaccination_center,
                "city":city,
                "state":state,
                "zip_code":zip_code,
            }
            request.session['datadict'] = datadict
            
            booking = Booking()
            booking.first_name = first_name
            booking.last_name = last_name
            booking.email = email
            booking.phone = phone
            booking.age = age
            booking.gender = gender
            booking.address = address
            booking.centre = vaccination_center
            booking.city = city
            booking.state = state
            booking.zip_code = zip_code
            booking.save() 
            data = {
                "msg": "The Booking for vaccine added successfully!!"
            }
        except:
            data = {
                "err": "An error occured in adding the Booking for vaccine"
            }
        return render(request,'appointment.html',data)
    else:
        return render (request, 'booking.html')


def appointment(request):
    if request.method == "POST":
        datadict=request.session.get('datadict')
        return render(request,'success.html',datadict)
    else:
        return render (request, 'appointment.html')
    

