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
        message = self.cleaned_data['message']
        email = self.cleaned_data['email']

        log_message = "Name: {0}, Email: {1}, Message: {2}".format(
            name,
            email,
            message,
        )

        logger.info(log_message)

        email_message = "Name: {0}\n Email: {1}\n\n, Message: {2}".format(
            name,
            email,
            message,
        )

        send_mail(
            '[Djangocph] Message from {0}'.format(email),
            email_message,
            'team@djangocph.com',
            ['team@djangocph.dk'],
            fail_silently=False
        )
        return True
