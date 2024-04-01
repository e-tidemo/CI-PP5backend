from django.urls import path
from .views import contact_us_view, contact_us_success
#from .views import csrf_token_view

urlpatterns = [
    #path('csrf-token/', csrf_token_view, name='csrf_token'),
    path('contact-us/', contact_us_view, name='contact_us'),
    path('contact-us/success/', contact_us_success, name='contact_us_success'),  # Success page URL
]
