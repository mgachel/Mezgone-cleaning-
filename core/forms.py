from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import ContactMessage, Booking


PHONE_PLACEHOLDER = 'e.g. (555) 123-4567'


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3', 'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3', 'placeholder': PHONE_PLACEHOLDER}),
            'subject': forms.Select(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3 text-foreground/80'}),
            'message': forms.Textarea(attrs={'class': 'min-h-[120px] w-full rounded-md border border-gray-300 px-3 py-2', 'placeholder': 'How can we help?', 'rows': 5}),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number (optional)',
            'subject': 'Subject',
            'message': 'Message',
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        # allow empty; basic sanity: at least 7 digits if provided
        digits = [c for c in phone if c.isdigit()]
        if phone and len(digits) < 7:
            raise ValidationError('Please enter a valid phone number or leave it blank.')
        return phone


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'service_type', 'first_name', 'last_name', 'email', 'phone',
            'address', 'preferred_date', 'preferred_time',
            'service_frequency', 'property_size', 'additional_notes'
        ]
        widgets = {
            'service_type': forms.Select(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3'}),
            'first_name': forms.TextInput(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3', 'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3', 'placeholder': PHONE_PLACEHOLDER}),
            'address': forms.TextInput(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3', 'placeholder': 'Street, City, ZIP'}),
            'preferred_date': forms.DateInput(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3', 'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3', 'type': 'time'}),
            'service_frequency': forms.Select(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3'}),
            'property_size': forms.Select(attrs={'class': 'h-12 w-full rounded-md border border-gray-300 px-3'}),
            'additional_notes': forms.Textarea(attrs={'class': 'min-h-[120px] w-full rounded-md border border-gray-300 px-3 py-2', 'placeholder': 'Any special instructions…', 'rows': 4}),
        }
        labels = {
            'service_type': 'Service Type',
            'preferred_date': 'Preferred Date',
            'preferred_time': 'Preferred Time',
            'service_frequency': 'Service Frequency',
            'property_size': 'Property Size',
            'additional_notes': 'Special Instructions or Requests',
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        digits = [c for c in phone if c.isdigit()]
        if len(digits) < 7:
            raise ValidationError('Please enter a valid phone number.')
        return phone

    def clean_preferred_date(self):
        date = self.cleaned_data.get('preferred_date')
        if date and date < timezone.localdate():
            raise ValidationError('Preferred date cannot be in the past.')
        return date