from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Booking, Contact
from .forms import ContactForm, BookingForm


# Create your views here.
def index(request):
    """landing page entry point"""
    print(request.user)
    print(request.user.email)
    print(dir(request.user))
    # We expect a GET request for the users email client
    if request.method != "GET":
        return HttpResponse(f"<h1>{request.method} is not accepted</h1>")

    return render(request, "restaurant/index.html", {})


@login_required
def profile(request):
    """profile page entry point"""
    # We expect a GET request for the users email client
    if request.method == "GET":
        profile = UserProfile.objects.filter(user=request.user).first()
        print(profile)
        if profile:
            context = {
                "firstname": profile.firstname,
                "lastname": profile.lastname,
            }
        else:
            context = {}
        return render(request, "restaurant/profile.html", context)

    if request.method == "POST":
        # Handle incoming form data
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        profile = UserProfile.objects.filter(user=request.user).first()
        if profile:
            profile.firstname = firstname
            profile.lastname = lastname
            profile.save()
        else:
            UserProfile(
                user=request.user,
                firstname=firstname,
                lastname=lastname,
                email=request.user.email,
            ).save()
        context = {
            "firstname": firstname,
            "lastname": lastname,
        }
        return render(request, "restaurant/profile.html", context)

    # For all other request types, return not accepted HTML code
    return HttpResponse(f"<h1>{request.method} is not accepted</h1>")


# Views for pages

"""Function to render contact hmtl page"""


def contact(request):
    return render(request, "restaurant/contact.html", {})


def contact_create(request):
    return render(request, "restaurant/contact_create.html", {})


"""Function to render menu hmtl page"""


def menu(request):
    return render(request, "restaurant/menu.html", {})


"""Function to render create booking page"""


@login_required
def create_booking(request):
    """Create a booking method"""
    # If user is not logged in then redirect to login page
    if not request.user.username:
        return redirect("/accounts/login/")

    form = BookingForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect("manage_bookings")
    context = {"user": request.user, "form": form}
    return render(request, "restaurant/create_booking.html", context)


def about(request):
    return render(request, "restaurant/about.html", {})


def index(request):
    return render(request, "restaurant/index.html", {})


# function for contact form view


def contact_create_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {"form": form}
    return render(request, "restaurant/contact_create.html", context)


# function for manage booking
@login_required
def manage_bookings(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        context = {"bookings": bookings}
    return render(request, "restaurant/manage_bookings.html", context)


# confirm delete booking function
@login_required
def confirm_delete_booking(request, booking_id):
    context = {"booking_id": booking_id}
    return render(request, "restaurant/confirm_delete_booking.html", context)


# delete booking function
@login_required
def delete_booking(request, booking_id):
    bookings = Booking.objects.get(pk=booking_id, user=request.user)
    bookings.delete()
    return render(request, "restaurant/success.html", {})


# update booking function
@login_required
def edit_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id, user=request.user)
    form = BookingForm(
        request.POST or None, request.FILES or None, instance=booking
    )
    if form.is_valid():
        booking.save()
        return redirect("manage_bookings")

    return render(
        request,
        "restaurant/edit_booking.html",
        {"booking": booking, "form": form},
    )


# change of booking confirmation details
@login_required
def booking_changed(request):
    return render(request, "restaurant/bookings_changed.html", {})


"""Function to render success page to show success flash message"""


@login_required
def success(request):
    return render(request, "restaurant/success.html", {})
