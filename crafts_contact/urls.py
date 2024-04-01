from django.urls import path
from .views import contact_us_view, contact_us_success, contact_form_view
from .views import csrf_token_view

urlpatterns = [
    path('csrf-token/', csrf_token_view, name='csrf_token'),
    path('contact-form/', contact_form_view, name='contact_form'),
    path('contact-us/', contact_us_view, name='contact_us'),
    path('contact-us/success/', contact_us_success, name='contact_us_success'),  # Success page URL
]
