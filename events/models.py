from django.db import models
from markdownx.models import MarkdownxField
from django.utils import timezone


class EventManager(models.Manager):

    def get_past_events(self):
        """
        Filtering by date, showing only show events before today
        """
        now = timezone.now()
        return self.get_queryset().filter(
            start_at__date__lt=now.date()
        ).order_by('start_at')

    def get_future_events(self):
        """
        Filtering by date, showing events `today` as well as future events
        """
        now = timezone.now()
        return self.get_queryset().filter(
            start_at__date__gte=now.date()
        ).order_by('start_at')


class Event(models.Model):
    """
    A simple model to keep track of past and future events
    """

    objects = EventManager()

    title = models.CharField(max_length=90)

    start_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True, null=True)

    about = MarkdownxField()

    location = models.TextField(blank=True)
    meedup_link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
