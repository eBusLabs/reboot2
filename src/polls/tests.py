import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
        
    def test__str__(self):
        """
        __str__ should return friendly name for Question() 
        """
        new_question = Question(pub_date=timezone.now(),question_text='new question')
        self.assertEqual(new_question.__str__(), 'new question')