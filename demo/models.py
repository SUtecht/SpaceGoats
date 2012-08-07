from django.db import models
import datetime
from django.utils import timezone
from django import forms
from django.forms.extras.widgets import SelectDateWidget



class Voter(models.Model):
	fname = models.CharField(max_length=100)
	mname = models.CharField(max_length=100, blank=True)
	lname = models.CharField(max_length=100)
	address = models.TextField()
	email = models.EmailField(max_length=254, blank=True)
	home_phone = models.CharField(max_length=100, blank=True)
	work_phone = models.CharField(max_length=100, blank=True)
	cell_phone = models.CharField(max_length=100, blank=True)
	loc_code = models.CharField(max_length=3)
	def __unicode__(self):
		return "{} {} {}".format(self.id, self.fname, self.lname )

	
		
class Event(models.Model):
	name = models.CharField(max_length=100)
	type = models.IntegerField()
	begin = models.DateTimeField()
	end = models.DateTimeField()
	completed = models.CharField(max_length=1)
	def __unicode__(self):
		return "{} {}".format(self.id, self.name)
		
class EventForm(forms.Form):
	name = forms.CharField(max_length=100, label='Event Name')
	type = forms.IntegerField( label='What type of event is this?')
	begin = forms.DateTimeField(widget=SelectDateWidget(),  label='When does the event start?')
	end = forms.DateTimeField(widget=SelectDateWidget(),  label='What is the estimate end date?')
		
class Term(models.Model):
	begin = models.DateTimeField()
	end = models.DateTimeField()
	def __unicode__(self):
		return "Term {} from {} to {}".format(self.id, self.begin, self.end )
		
class Pool(models.Model):
	term = models.ForeignKey(Term)
	name = models.CharField(max_length=100)
	parent_pool =  models.ForeignKey('self', blank=True, null=True)
	def __unicode__(self):
		return "{} {} ".format(self.id, self.name)


class Pool_Member(models.Model):
	voter = models.ForeignKey(Voter)
	pool = models.ForeignKey(Pool)
	status =  models.IntegerField()
	def __unicode__(self):
		return "{} {} ".format(self.voter, self.pool)
	
	
class Transaction(models.Model):
	pool_member = models.ForeignKey(Pool_Member)
	event = models.ForeignKey(Event)
	payment_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
	processed =  models.CharField(max_length=1)
	def __unicode__(self):
		return "{} {} {}".format(self.pool_member, self.event, self.payment_ammount)