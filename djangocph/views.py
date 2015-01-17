from django.views.generic.edit import FormView
from django.contrib import messages


from . import forms


class IndexView(FormView):
    template_name = 'base.html'
    form_class = forms.ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        msg = "We have received your message, we will now decide your fate"
        messages.add_message(self.request, messages.INFO, msg)
        return super(IndexView, self).form_valid(form)
