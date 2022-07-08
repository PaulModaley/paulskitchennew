from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("contact/", views.contact, name="contact"),
    path("menu/", views.menu, name="menu"),
    path("create_booking/", views.create_booking, name="create_booking"),
    path("about/", views.about, name="about"),
    path("contact_create/", views.contact_create_view, name="contact_create"),
    path("manage_bookings/", views.manage_bookings, name="manage_bookings"),
    path(
        "confirm_delete_booking/<int:booking_id>",
        views.confirm_delete_booking,
        name="confirm_delete_booking",
    ),
    path(
        "delete_booking/<int:booking_id>",
        views.delete_booking,
        name="delete_booking",
    ),
    path(
        "edit_booking/<int:booking_id>",
        views.edit_booking,
        name="edit_booking",
    ),
    path("booking_changed/", views.booking_changed, name="booking_changed"),
    path("success/", views.success, name="success"),
]
