from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from . import forms


class Website(TemplateView):
    template_name = 'website.html'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = forms.ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)