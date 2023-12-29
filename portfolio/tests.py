from django.core import mail
from django.urls import reverse
from django.test import TestCase, override_settings
from django.http import HttpResponsePermanentRedirect

@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class PortfolioTestCase(TestCase):
    def test_resume_url(self):
        response = self.client.get(reverse('resume'))
        self.assertEqual(response.status_code, 200)

    def test_projects_url(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

    def test_contact_url(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200) 

    def test_linkedin_redirect(self):
        response = self.client.get(reverse('linkedin'))
        self.assertIsInstance(response, HttpResponsePermanentRedirect)
        self.assertEqual(response.url, 'https://www.linkedin.com/in/adithya-rajendran/')

    def test_github_redirect(self):
        response = self.client.get(reverse('github'))
        self.assertIsInstance(response, HttpResponsePermanentRedirect)
        self.assertEqual(response.url, 'https://github.com/Adithya-Rajendran')

    def test_contact_form_submission(self):
        # Define test data
        test_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '+12015550123',
            'message': 'This is a test message.',
        }

        # Simulate a POST request to the contact form view
        response = self.client.post(reverse('contact'), test_data, follow=True)

        # Check if the form submission was successful
        self.assertEqual(response.status_code, 200) 

        # Check if the success message is present in the response content
        self.assertContains(response, 'Your message was successfully submitted!')

        # Check if the email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Contact Form for My Website')

        # Check if the email contains the expected content
        self.assertIn('John Doe', mail.outbox[0].body)
        self.assertIn('john@example.com', mail.outbox[0].body)
        self.assertIn('+12015550123', mail.outbox[0].body)
        self.assertIn('This is a test message.', mail.outbox[0].body)
