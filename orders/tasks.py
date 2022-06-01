from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_create_task(order_id):
    """
        task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id = order_id)
    subject = 'order nr. {}'.format(order.id)
    message = 'Dear {},\n\n you have successfully placed an order. your order is {}'.format(order.id)
    mail_sent = send_mail(subject, message, "admin@admin.com", [order.email])
    return mail_sent
