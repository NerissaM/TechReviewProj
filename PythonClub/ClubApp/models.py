from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    titleid=models.CharField(max_length=225)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=225)
    agenda=models.CharField(max_length=225)

    def __str__(self):
        return self.titleid

    class Meta:
        db_table='Meeting' 
        verbose_name_plural='Meetings'

class MeetingMinute(models.Model):
    durationid=models.CharField(max_length=255)
    meetingid =models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    
    def __str__(self): 
        return self.durationid

    class Meta:
        db_table='MeetingMinute'
        verbose_name_plural='meetingminutes' 

class Resource(models.Model):
    resourceid=models.CharField(max_length=255)
    resourcefield=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.resourceid

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventid=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.eventid

    class Meta:
        db_table='event'
        verbose_name_plural='events'

