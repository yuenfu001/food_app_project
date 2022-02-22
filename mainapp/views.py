from django.shortcuts import render
from django.http import HttpResponse

from mainapp.models import Customer

# Create your views here.
def home(request):
    # return HttpResponse("Hello world! welcome to this food application")
    customer = Customer.objects.all()


    return render(request,'home.html',{'cus':customer})
