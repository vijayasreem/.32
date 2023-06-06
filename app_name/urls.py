from django.urls import path

urlpatterns = [
    path('send_welcome_email/', send_welcome_email),
    path('send_password_reset_email/', send_password_reset_email),
    path('send_order_confirmation_email/', send_order_confirmation_email),
    path('send_account_activity_alert_email/', send_account_activity_alert_email),
    path('log_email_status/', log_email_status),
    path('monitor_email_delivery/', monitor_email_delivery),
]