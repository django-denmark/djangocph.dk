from django.test import TestCase
from django.utils import timezone
from .models import Event


class EventManagerTests(TestCase):

    def setUp(self):
        self.past = timezone.make_aware(timezone.datetime(2001, 1, 1))
        self.future = timezone.make_aware(timezone.datetime(2101, 1, 1))
        self.now = timezone.now()

    def test_managers(self):
        in_past = Event.objects.create(
            title='title',
            start_at=self.past
        )
        in_future = Event.objects.create(
            title='title',
            start_at=self.future
        )

        events = Event.objects.get_past_events()

        self.assertEquals(events.count(), 1)
        self.assertTrue(in_past in events)
        self.assertFalse(in_future in events)

        events = Event.objects.get_future_events()

        self.assertEquals(events.count(), 1)
        self.assertFalse(in_past in events)
        self.assertTrue(in_future in events)

    def test_today_event_is_in_future(self):
        """
        Showing events today together with future events
        """
        today = Event.objects.create(
            title='title',
            start_at=self.now
        )

        events = Event.objects.get_past_events()

        self.assertEquals(events.count(), 0)

        events = Event.objects.get_future_events()

        self.assertEquals(events.count(), 1)
        self.assertTrue(today in events)
