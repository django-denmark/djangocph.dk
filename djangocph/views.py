from django.views.generic import FormView
from django.contrib import messages
from django.conf import settings
from akismet import Akismet
from events.models import Event

from . import forms


class IndexView(FormView):
    template_name = 'base.html'
    form_class = forms.ContactForm
    success_url = '/'

    def is_spam(self, form):
        """
        Is Akismet still a thing?
        Lets try to limit the spam if people supply a key
        """
        if not settings.AKISMET_KEY:
            return False

        akismet = Akismet(
            settings.AKISMET_KEY, blog=self.request.get_host()
        )

        agent = self.request.META.get('HTTP_USER_AGENT')
        referrer = self.request.META.get('HTTP_REFERER')
        ip = self.request.META.get('REMOTE_ADDR')
        check = akismet.check(
              ip, agent,
              comment_author_email=form.cleaned_data['email'],
              comment_content=form.cleaned_data['message'],
        )
        return check

    def form_valid(self, form):
        if not self.is_spam(form):
            form.send_email()
        msg = "We have received your message, we will now decide your fate"
        messages.add_message(self.request, messages.INFO, msg)
        return super(IndexView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['past_events'] = Event.objects.get_past_events()
        kwargs['future_events'] = Event.objects.get_future_events()
        return super().get_context_data(**kwargs)
