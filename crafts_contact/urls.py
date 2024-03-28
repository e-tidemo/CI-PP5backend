from django.urls import path
from .views import ContactAPIView, SubmitContactFormView

urlpatterns = [
    path('submit_contact_form/', SubmitContactFormView.as_view(), name='submit_contact_form'),
]

"""
urlpatterns = [
    path('contact-us/', contact_us_view, name='contact_us'),  # For rendering HTML
    path('api/contact-us/', ContactAPIView.as_view(), name='contact_us_api'),  # For handling API requests
]
"""
