from django.urls import path
from .views import contact_us_view, contact_us_success

urlpatterns = [
    path('contact-us/', contact_us_view, name='contact_us'),
    path('contact-us/success/', contact_us_success, name='contact_us_success'),  # Success page URL
]
