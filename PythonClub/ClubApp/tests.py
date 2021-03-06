from django.test import TestCase
from .models import Meeting, MeetingMinute, Resource, Event

# Create your tests here.
class MeetingTest(TestCase):
   def test_string(self):
       type=Meeting(titleid="Meeting")
       self.assertEqual(str(type), type.titleid)

   def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class MeetingMinuteTest(TestCase):
   def test_string(self):
       type=MeetingMinute(durationid="1")
       self.assertEqual(str(type), type.durationid)

   def test_table(self):
       self.assertEqual(str(MeetingMinute._meta.db_table), 'MeetingMinute')

class ResourceTest(TestCase):
   def test_string(self):
       type=Resource(resourceid="4")
       self.assertEqual(str(type), type.resourceid)

   def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')