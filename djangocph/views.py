from django.views.generic import TemplateView


class Website(TemplateView):
    template_name = 'website.html'
