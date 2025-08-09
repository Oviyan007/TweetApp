from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.signing import TimestampSigner
from django.core.mail import send_mail
from django.urls import reverse

signer = TimestampSigner()

@receiver(post_save, sender=User)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        # Create signed token
        token = signer.sign(instance.username)
        
        # Confirmation URL
        confirmation_link = f"http://127.0.0.1:8000/confirm-email/{token}/"
        
        # Send Email
        send_mail(
            subject="Confirm your Email - Django Project",
            message=f"Hi {instance.username},\n\nClick the link below to confirm your email:\n{confirmation_link}",
            from_email="your_email@gmail.com",
            recipient_list=[instance.email],
            fail_silently=False,
        )
