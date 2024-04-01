from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm

@csrf_exempt
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
