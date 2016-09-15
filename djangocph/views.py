from django.views.generic.edit import FormView
from django.contrib import messages

from events.models import Event

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

    def get_context_data(self, **kwargs):
        kwargs['past_events'] = Event.objects.get_past_events()
        kwargs['future_events'] = Event.objects.get_future_events()
        return super().get_context_data(**kwargs)
