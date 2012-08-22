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
		return "{} {} {}".format(self.fname, self.mname, self.lname )

	
		
class Event(models.Model):
	name = models.CharField(max_length=100)
	begin = models.DateTimeField()
	end = models.DateTimeField()
	completed = models.CharField(max_length=1)
	pools = models.ManyToManyField('Pool', blank=True,null=True)
	def __unicode__(self):
		return "{} {}".format(self.id, self.name)
		
class EventForm(forms.Form):
	name = forms.CharField(max_length=100)
	begin_date = forms.CharField( )
	begin_time = forms.CharField(max_length=10)
	end_date = forms.CharField( )
	end_time = forms.CharField(max_length=10)
		
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
		return "{} {} ".format(self.voter, self.status)
		
class NewPoolForm(forms.Form):
	pool_term = forms.ModelChoiceField(Term.objects.all())
	pool_name = forms.CharField(max_length=100)
	number_of_members = forms.IntegerField()
	
class OldPoolForm(forms.Form):
	pool_name = forms.ModelChoiceField(Pool.objects.all())
	
class Transaction(models.Model):
	pool_member = models.ForeignKey(Pool_Member)
	event = models.ForeignKey(Event)
	payment_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
	processed =  models.CharField(max_length=1)
	def __unicode__(self):
		return "{} {} {}".format(self.pool_member, self.event, self.payment_ammount)