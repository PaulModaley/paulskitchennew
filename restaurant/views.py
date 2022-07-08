from django.shortcuts import render, HttpResponse
from .models import UserProfile, Booking

# Create your views here.
def index(request):
    """landing page entry point"""
    print(request.user)
    print(request.user.email)
    print(dir(request.user))
    # We expect a GET request for the users email client
    if request.method != "GET":
        return HttpResponse(f"<h1>{request.method} is not accepted</h1>")

    return render(request, 'restaurant/index.html', {})

def profile(request):
    """profile page entry point"""
    # We expect a GET request for the users email client
    if request.method == "GET":
        profile = UserProfile.objects.all()
        print(profile)
        return render(request, 'restaurant/profile.html', {})

    if request.method == "POST":
        #Handle incoming form data
        return render(request, 'restaurant/profile.html', {})


      #For all other request types, return not accepted HTML code  
    return HttpResponse(f"<h1>{request.method} is not accepted</h1>")