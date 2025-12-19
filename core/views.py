from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm, BookingForm


# Create your views here.

def home(request):
    # Render the existing template (index.html) instead of non-existent home.html
    return render(request, 'index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            messages.success(request, 'Thanks! Your message has been sent. We\'ll get back to you within 24 hours.')
            # fresh form after success
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form, 'success': success})

def services(request):
    # Use the Django-templated version under pages/
    return render(request, 'pages/services.html')

def booking(request):
    success = False
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            messages.success(request, 'Your booking request was submitted successfully! We\'ll confirm details shortly.')
            form = BookingForm()
    else:
        form = BookingForm()
    return render(request, 'pages/booking.html', {'form': form, 'success': success})
