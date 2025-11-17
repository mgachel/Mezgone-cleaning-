from django.contrib import admin
from .models import ContactMessage, Booking


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "subject", "created_at")
	list_filter = ("subject", "created_at")
	search_fields = ("name", "email", "message")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "service_type", "preferred_date", "created_at")
	list_filter = ("service_type", "service_frequency", "property_size", "preferred_date", "created_at")
	search_fields = ("first_name", "last_name", "email", "address")
