import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class AutoPainter(models.Model):
    class_name = models.CharField(max_length=100)
    begin_stroke = models.CharField(max_length=4096)
    follow_stroke = models.CharField(max_length=4096)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "class_name: {0}, begin_stroke: {1}, follow_stroke: {2}, " \
               "pub_date: {3}.".format(self.class_name, self.begin_stroke,
                                       self.follow_stroke, self.pub_date)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
