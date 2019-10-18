from django.shortcuts import render, redirect
from .forms import ContactForm, ReservationForm
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Reservation
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    Success = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            cd = form.cleaned_data
            message = 'The Mail is from {}... The Message is {} .. Email is {}'.format(cd['name'], cd['message'], cd['from_email'])
            
            try:
                send_mail(subject, message, from_email, ['admin@admin.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            Success['success'] = "We have recieved your message successfully."
            return redirect('contactsuccess')
            
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form, 'Success':Success})

def reservation(request):
    return render(request, 'reservation.html')

def rervationsuccessful(request):
    return render(request, 'rervationsuccessful.html')


class ReservationView(CreateView):
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('rervationsuccessful')

class contactSuc(TemplateView):
    template_name = 'contactsuccess.html'



