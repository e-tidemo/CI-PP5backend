from django.conf import settings
from django.db import models
from django.core.validators import validate_email, MinLengthValidator

class Contact(models.Model):
    class ContactChoices(models.TextChoices):
        REPORT = "1", "Business inquiries"
        BUSINESS = "2", "Report user"
        FEEDBACK = "3", "Feedback about website"
        OTHER = "4", "Other questions"
    
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Name',
        help_text='Name'
    )
    email = models.EmailField(
        validators=[validate_email],
        blank=False
    )
    subject = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Email subject',
        help_text='Email subject.'
    )
    message = models.TextField(
        max_length=2200,
        null=False,
        blank=False, 
        verbose_name='Email message',
        help_text='Email message',
        validators=[MinLengthValidator(5)]
    )
    ContactChoices = models.CharField(
        max_length=1,
        choices=ContactChoices.choices,
        default=ContactChoices.OTHER,
        null=False
    )

    def __str__(self):
        # Return the sender's name and the subject of the email.
        return self.name + " - " + self.subject
    
    class Meta:
        verbose_name = 'Messages to admin of World of Craft'
        verbose_name_plural = 'Messages to admin of World of Craft'
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)