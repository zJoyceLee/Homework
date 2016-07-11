import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Form

from django.core.urlresolvers import reverse

# Create your tests here.

class FormMethodTests(TestCase):

    def test_was_published_recently_with_future_form(self):
        """
        was_published_recently() should return False for forms whose
        pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_form = Form(pub_date=time)
        self.assertEqual(future_form.was_published_recently(), False)


    def test_was_published_recently_with_recent_form(self):
        """
        was_published_recently() should return True for form whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_form = Form(pub_date=time)
        self.assertEqual(recent_form.was_published_recently(), True)


        def create_form(form_text, days):
    """
    Creates a form with the given 'form_text' and published the
    given number of 'days' offset to now (nogative for forms published
    in the past, positive for forms that have yet to be published).
    """
    time =  timezone.now() + datetime.timedelta(days=days)
    return Form.objects.create(form_text=form_text, pub_date=time)


class FormViewTests(TestCase):
    def test_index_view_with_no_form(self):
        """
        If no forms exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
