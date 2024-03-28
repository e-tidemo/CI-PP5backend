from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.validators import validate_email
from django.core.validators import MinLengthValidator


# Some help with choices field option was collected 
# from https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django
# Some help with understanding EmailMultiAlternatives 
# was given by my mentor, Julia, and her project in e-commerce:
# https://github.com/IuliiaKonovalova/e-commerce/blob/main/email_notifications/models.py
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
        validators=[MinLengthValidator(5)])
    code = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Code',
        help_text='Code.'
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
        verbose_name = 'Email to admin of World of Craft'
        verbose_name_plural = 'Emails to admin of World of Craft'

    def save(self, *args, **kwargs):
        super().save()
        recipients = [settings.EMAIL_HOST_USER],
        subject = self.subject,
        from_email = self.email,
        text_content = ''
        if self.code is not None:
            html_content = (
                '<h1 style="text-align:center">' +
                self.name +
                '</h1><br><p style="text-align:center">'
                'wants to send a message regarding'
                '</p>' + self.ContactChoices + '<p>'
                'They say </p>' + self.message
            )
        else:
            html_content = (
                '<h1 style="text-align:center>' +
                self.name +
                '</h1><br><p>' + self.message + '</p>'
                '<p>' + 'On the subject of' + 
                self.ContactChoices + '</p>'
            )

        msg = EmailMultiAlternatives(subject, text_content, from_email, recipients)
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
   