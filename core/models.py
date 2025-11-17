from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=200, choices=[
        ('general', 'General Inquiry'),
        ('service', 'Service Request'),
        ('feedback', 'Feedback'),
        ('other', 'Other'),
    ])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    
class Booking(models.Model):
    service_type = models.CharField(max_length=50, choices=[
        ('residential', 'Residential Cleaning'),
        ('commercial', 'Commercial Cleaning'),
        ('deep_cleaning', 'Deep Cleaning'),
        ('move_in_out', 'Move In/Out Cleaning'),
    ])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    service_frequency = models.CharField(max_length=50, choices=[
        ('one_time', 'One-Time Service'),
        ('weekly', 'Weekly Service'),
        ('bi_weekly', 'Bi-Weekly Service'),
        ('monthly', 'Monthly Service'),
    ])
    property_size = models.CharField(max_length=50, choices=[
        ('small', 'Small (up to 1000 sqft)'),
        ('medium', 'Medium (1000-2500 sqft)'),
        ('large', 'Large (2500+ sqft)'),
    ])
    additional_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.first_name} {self.last_name} on {self.preferred_date}"
    













