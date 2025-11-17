from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage, Booking
from datetime import date, timedelta


class ContactFormViewTests(TestCase):
	def test_contact_get(self):
		resp = self.client.get(reverse('contact'))
		self.assertEqual(resp.status_code, 200)
		self.assertIn('form', resp.context)

	def test_contact_post_valid(self):
		payload = {
			'name': 'Alice',
			'email': 'alice@example.com',
			'phone': '',
			'subject': 'general',
			'message': 'Hello there',
		}
		resp = self.client.post(reverse('contact'), payload, follow=True)
		self.assertEqual(resp.status_code, 200)
		self.assertTrue(ContactMessage.objects.filter(email='alice@example.com').exists())

	def test_contact_post_invalid_email(self):
		payload = {
			'name': 'Bob',
			'email': 'not-an-email',
			'phone': '',
			'subject': 'general',
			'message': 'Test',
		}
		resp = self.client.post(reverse('contact'), payload)
		self.assertEqual(resp.status_code, 200)
		self.assertFormError(resp, 'form', 'email', 'Enter a valid email address.')


class BookingFormViewTests(TestCase):
	def test_booking_get(self):
		resp = self.client.get(reverse('booking'))
		self.assertEqual(resp.status_code, 200)
		self.assertIn('form', resp.context)

	def test_booking_post_valid(self):
		tomorrow = date.today() + timedelta(days=1)
		payload = {
			'service_type': 'residential',
			'first_name': 'John',
			'last_name': 'Doe',
			'email': 'john@example.com',
			'phone': '5551234567',
			'address': '123 Main St',
			'preferred_date': tomorrow.isoformat(),
			'preferred_time': '10:00',
			'service_frequency': 'one_time',
			'property_size': 'small',
			'additional_notes': '',
		}
		resp = self.client.post(reverse('booking'), payload, follow=True)
		self.assertEqual(resp.status_code, 200)
		self.assertTrue(Booking.objects.filter(email='john@example.com').exists())

	def test_booking_post_past_date_invalid(self):
		yesterday = date.today() - timedelta(days=1)
		payload = {
			'service_type': 'residential',
			'first_name': 'Jane',
			'last_name': 'Doe',
			'email': 'jane@example.com',
			'phone': '5551234567',
			'address': '456 Oak St',
			'preferred_date': yesterday.isoformat(),
			'preferred_time': '10:00',
			'service_frequency': 'one_time',
			'property_size': 'small',
			'additional_notes': '',
		}
		resp = self.client.post(reverse('booking'), payload)
		self.assertEqual(resp.status_code, 200)
		self.assertFormError(resp, 'form', 'preferred_date', 'Preferred date cannot be in the past.')
