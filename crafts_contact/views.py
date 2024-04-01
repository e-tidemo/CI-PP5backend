from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
from django.middleware.csrf import get_token
from django.http import JsonResponse

def csrf_token_view(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})

@csrf_protect
def contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us_success')  # Redirect to a success page or URL
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

def contact_us_success(request):
    return render(request, 'contact_us_success.html')

def contact_form_view(request):
    return render(request, 'contact_form.html')

