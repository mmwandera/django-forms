from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.

# Home Page View Function
def home_view(request):
    return render(request, 'form_app/home.html')

# Define the contct_view function to handle the contact form
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'form_app/contact.html', context)

# Define the contact_success_view function to handle the success page
def contact_success_view(request):
    return render(request, 'form_app/contact_success.html')