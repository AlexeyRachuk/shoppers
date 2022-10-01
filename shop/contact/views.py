from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import ContactFormPage


# Представление успешной отправки формы
def contact_success(request):
    return render(request, 'contact/contact_success.html')


# Представление формы на странице контактов
def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact_success'))
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html',
                  {'form': form, 'contacts': ContactFormPage.objects.all()})
