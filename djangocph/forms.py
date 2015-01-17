from django import forms
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name'],
        msg = self.cleaned_data['message']
        email = self.cleaned_data['email']

        msg = "Name: {0}, Email: {1}, Message: {2}".format(
            name,
            email,
            msg,
        )

        logger.info(msg)

        msg = "Name: {0}\n Email: {1}\n\n, Message: {2}".format(
            name,
            email,
            msg,
        )

        send_mail(
            'Message from {0}'.format(email), msg, 'team@djangocph.com',
            ['team@djangocph.dk'], fail_silently=False
        )
        return True
