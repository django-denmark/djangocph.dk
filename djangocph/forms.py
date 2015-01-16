from django import forms
import logging

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        msg = "Name: {0}, Message: {1}".format(self.name, self.message)
        logger.info(msg)
        return True