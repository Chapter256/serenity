from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import ContactForm


class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'contact.html',
            {
                'contact_form': ContactForm()
            }
        )

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for contacting Serenity Spa, we will get back to you as soon as possible.')
        else:
            contact_form = ContactForm()
        return render(
            request,
            'contact.html',
            {
                'contact_form': ContactForm()
            }
        )