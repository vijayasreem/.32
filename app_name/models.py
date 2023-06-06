from django.db import models
from django.core.mail import send_mail

class EmailNotification(models.Model):
    """Model to represent an email notification"""
    subject = models.CharField(max_length=100)
    body = models.TextField()
    recipients = models.ManyToManyField('User')
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')

    def send(self):
        """Sends the email notification to all recipients"""
        for recipient in self.recipients.all():
            try:
                send_mail(
                    self.subject,
                    self.body,
                    from_email=None,
                    recipient_list=[recipient.email],
                )
            except Exception as e:
                # Log the error and update the status
                self.status = 'error'
                self.save()
                return False
        # Update the status
        self.status = 'sent'
        self.save()
        return True

class User(models.Model):
    """Model to represent a user"""
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def send_welcome_email(self):
        """Sends a welcome email to the user upon successful registration"""
        subject = 'Welcome!'
        body = 'Welcome to our app, {}!'.format(self.first_name)
        EmailNotification.objects.create(subject=subject, body=body, recipients=[self])