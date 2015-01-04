from django.db import models
import datetime

class Location(models.Model):
	location_name = models.CharField(max_length=50)
	location_lon = models.FloatField(default=0)
	location_lat = models.FloatField(default=0)
	def __unicode__(self):
		return self.location_name

class Cup(models.Model):
	lister_name = models.CharField(max_length=50)
	location = models.ForeignKey(Location)
	topic = models.CharField(max_length=50)
	timestamp = models.DateTimeField('Time')
	def __unicode__(self):
		return self.lister_name + "--" + self.topic

	def get_time(self):
		t = self.timestamp - datetime.timedelta(hours=8) #change UTC to PST???
		date_string = ""
		date_string += str(t.day)
		date_string += " " + '{0:%B}'.format(t)[:3]
		hour = t.hour
		am = True
		if hour >= 12:
			hour -= 12
			am = False
		if hour == 0:
			hour = 12
		date_string += " " + str(hour) + ":"
		if t.minute < 10:
			date_string += "0"
		date_string += str(t.minute)
		date_string += "AM" if am else "PM"
#		date_string += " PST"
		return date_string