from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Contact


def contact(request):
    if request.method == 'POST':
        form_data = Contact(
            name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'], message=request.POST['message'])
        form_data.save()
        return redirect('/contact')
    return render(request, 'contact/contact_us.html')


def feedback(request):
    form_data = Contact.objects.all()
    return render(request, 'contact/feedback.html', {'form_data': form_data})


def delete_feedback(request, id):
    contact_details = Contact.objects.get(id=id)
    contact_details.delete()
    return redirect('/contact/feedback')
