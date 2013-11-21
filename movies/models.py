#TODO: cleanup imports, not sure if we will use all of datetime etc...
import datetime
from django.db import models


class Movie(models.Model):
    """A movie and it's related information. A movie can have 0 or more Actors."""

    title = models.CharField(max_length=2000)
    #Could have used TextField here...
    description = models.CharField(max_length=4000)
    opening_date = models.DateTimeField('date opened')
    created_at = models.DateTimeField('created date', auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('opening_date',)


class Actor(models.Model):
    """Information about an Actor including derived fields."""

    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    stage_name = models.CharField(max_length=500, null=True)
    #We will just assume we know all actors DOB, not realistic, but fine assumption for this project
    birth_date = models.DateTimeField('date born')
    movies = models.ManyToManyField(Movie)
    biography = models.CharField(max_length=2000, null=True)

    def __unicode__(self):
        if self.stage_name:
            return '%s (%s)' % (self.stage_name, self.full_name('fmil'))
        else:
            return self.full_name()

    def full_name(self, name_order='lfm'):
        #TODO: Clunky way of doing this. Optimize if time.
        if name_order == 'fml':
            if self.middle_name:
                return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)
            else:
                return '%s %s' % (self.first_name, self.last_name)
        elif name_order == 'lfmi':
            if self.middle_name:
                return '%s, %s %s' % (self.last_name, self.first_name, self.middle_initial())
            else:
                return '%s, %s' % (self.last_name, self.first_name)
        elif name_order == 'fmil':
            if self.middle_name:
                return '%s %s %s' % (self.first_name, self.middle_initial(), self.last_name)
            else:
                return '%s %s' % (self.first_name, self.last_name)
        elif name_order == 'lfm':
            if self.middle_name:
                return '%s, %s %s' % (self.last_name, self.first_name, self.middle_name)
            else:
                return '%s, %s' % (self.last_name, self.first_name)
        else:
            raise Exception('Unknown name format: %s') % name_order

    def middle_initial(self):
        if self.middle_name:
            return self.middle_name[0] + '.'
        else:
            return None

    def age(self):
        today = datetime.date.today()
        try:  # deal with leap years
            birthday = self.birth_date.replace(year=today.year)
        except ValueError:
            birthday = self.birth_date.replace(year=today.year, day=self.birth_date.day-1)
        if birthday > today:
            return today.year - self.birth_date.year - 1
        else:
            return today.year - self.birth_date.year

    class Meta:
        ordering = ('last_name',)