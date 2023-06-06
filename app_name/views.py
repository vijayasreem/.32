from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(user):
    subject = 'Welcome to our site!'
    message = 'Thanks for joining our site, {}!'.format(user.username) 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail( subject, message, email_from, recipient_list )

def send_password_reset_email(user):
    subject = 'Password reset request'
    message = 'Hi {},\n\nWe received a request to reset your password. If you did not request a password reset, please ignore this email.\n\nOtherwise, click the link below to reset your password:\n\n{}'.format(user.username, reset_url)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail( subject, message, email_from, recipient_list )

def send_order_confirmation_email(user, order):
    subject = 'Order Confirmation'
    message = 'Hi {},\n\nThank you for your order! Your order details are below:\n\nOrder Number: {}\nTotal: ${}\nItems: {}'.format(user.username, order.order_number, order.total, order.items)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail( subject, message, email_from, recipient_list )

def send_account_activity_alert_email(user):
    subject = 'Account Activity Alert'
    message = 'Hi {},\n\nWe noticed unusual activity on your account. If you did not take any of these actions, please contact us immediately.'.format(user.username)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail( subject, message, email_from, recipient_list )

def log_email_status(user, message):
    # Log the email status for the user
    pass

def monitor_email_delivery():
    # Monitor email delivery and handle any errors
    pass