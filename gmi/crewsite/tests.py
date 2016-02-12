from django.core.urlresolvers import reverse
from django.test import TestCase


class CrewViewTestCase(TestCase):
    def test_index(self):
        response = self.client.get(reverse('crewsite:index'))
        self.assertRedirects(
            response,
            reverse('zinnia:entry_archive_index'),
            status_code=301)
