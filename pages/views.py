from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
from django.shortcuts import render
def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject=f"Fithub Contact Form: {name}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'pages/contact.html')